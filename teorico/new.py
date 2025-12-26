# =============================================================================
# SCRIPT "TUDO EM UM" PARA CLASSIFICAÇÃO DE ESPECTROGRAMAS
# =============================================================================

import os
import shutil
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from PIL import Image

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# =============================================================================
# SEÇÃO 1: CONFIGURAÇÃO (o que estava em config.py)
# =============================================================================
print("Configurando parâmetros do projeto...")

# Parâmetros de Dados
# As pastas 'raw', 'processed' e 'models' serão criadas dentro de 'data'
RAW_DATA_PATH = "data/raw"
PROCESSED_DATA_PATH = "data/processed"
IMAGE_SIZE = 128

# Parâmetros do Espectrograma
CMAP = 'gray'

# Parâmetros de Treinamento
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
BATCH_SIZE = 32
EPOCHS = 25
LEARNING_RATE = 0.001
VALIDATION_SPLIT = 0.2

# Parâmetros do Modelo
MODELS_DIR = "models"
MODEL_PATH = os.path.join(MODELS_DIR, "espectrograma_cnn_v1.pth")


# =============================================================================
# SEÇÃO 2: DEFINIÇÃO DO MODELO (o que estava em model.py)
# =============================================================================
class SpectrogramCNN(nn.Module):
    def __init__(self, num_classes=2):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1)
        
        final_dim = IMAGE_SIZE // (2**3)
        self.fc1 = nn.Linear(64 * final_dim * final_dim, 512)
        self.fc2 = nn.Linear(512, num_classes)
        self.dropout = nn.Dropout(0.5)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))
        x = x.view(x.size(0), -1)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x

# =============================================================================
# SEÇÃO 3: PREPARAÇÃO DOS DADOS (de 01_prepare_data.py)
# =============================================================================
def create_spectrogram(wav_path, save_path):
    try:
        fs, data = wavfile.read(wav_path)
        if data.ndim > 1: data = data[:, 0]
        if np.max(np.abs(data)) == 0: return False # Ignora arquivos vazios
        data = data / np.max(np.abs(data))

        plt.figure(figsize=(IMAGE_SIZE/100, IMAGE_SIZE/100), dpi=100)
        plt.specgram(data, NFFT=1024, Fs=fs, noverlap=512, cmap=CMAP)
        plt.axis('off')
        plt.savefig(save_path, bbox_inches='tight', pad_inches=0)
        plt.close()
        return True
    except Exception as e:
        print(f"  - Erro ao processar {wav_path}: {e}")
        return False

def process_all_audio():
    print("\n--- ETAPA 1: Preparando Dados (WAV -> PNG) ---")
    if os.path.exists(PROCESSED_DATA_PATH):
        shutil.rmtree(PROCESSED_DATA_PATH)
    
    if not os.path.exists(RAW_DATA_PATH) or not any(os.scandir(RAW_DATA_PATH)):
        print(f"ERRO: Pasta '{RAW_DATA_PATH}' não encontrada ou vazia.")
        print("Por favor, crie a pasta e coloque seus arquivos .wav dentro de subpastas de classe.")
        return False

    for class_name in os.listdir(RAW_DATA_PATH):
        raw_class_path = os.path.join(RAW_DATA_PATH, class_name)
        if not os.path.isdir(raw_class_path): continue
            
        audio_files = [f for f in os.listdir(raw_class_path) if f.endswith('.wav')]
        random.shuffle(audio_files)
        
        split_idx = int(len(audio_files) * (1 - VALIDATION_SPLIT))
        train_files, val_files = audio_files[:split_idx], audio_files[split_idx:]
        
        print(f"Processando classe '{class_name}': {len(train_files)} treino, {len(val_files)} validação.")
        for split_name, files in [('train', train_files), ('validation', val_files)]:
            dest_dir = os.path.join(PROCESSED_DATA_PATH, split_name, class_name)
            os.makedirs(dest_dir, exist_ok=True)
            for file_name in files:
                wav_path = os.path.join(raw_class_path, file_name)
                png_name = os.path.splitext(file_name)[0] + '.png'
                save_path = os.path.join(dest_dir, png_name)
                create_spectrogram(wav_path, save_path)
                
    print("Preparação dos dados concluída!")
    return True

# =============================================================================
# SEÇÃO 4: TREINAMENTO DO MODELO (de 02_train.py)
# =============================================================================
def train_model():
    print("\n--- ETAPA 2: Treinando o Modelo ---")
    
    transform = transforms.Compose([
        transforms.Grayscale(),
        transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])

    try:
        train_dataset = datasets.ImageFolder(root=os.path.join(PROCESSED_DATA_PATH, 'train'), transform=transform)
        val_dataset = datasets.ImageFolder(root=os.path.join(PROCESSED_DATA_PATH, 'validation'), transform=transform)
    except FileNotFoundError:
        print("ERRO: Pastas de treino/validação não encontradas. A preparação de dados falhou.")
        return
        
    train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE, shuffle=False)

    num_classes = len(train_dataset.classes)
    model = SpectrogramCNN(num_classes=num_classes).to(DEVICE)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

    print(f"Dispositivo de treino: {DEVICE}")
    print(f"Classes encontradas: {train_dataset.classes}")
    print(f"Iniciando o treinamento para {EPOCHS} épocas...")

    for epoch in range(EPOCHS):
        model.train()
        running_loss = 0.0
        for images, labels in train_loader:
            images, labels = images.to(DEVICE), labels.to(DEVICE)
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()

        model.eval()
        correct, total = 0, 0
        with torch.no_grad():
            for images, labels in val_loader:
                images, labels = images.to(DEVICE), labels.to(DEVICE)
                outputs = model(images)
                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()
        
        accuracy = 100 * correct / total
        avg_loss = running_loss / len(train_loader)
        print(f"Época [{epoch+1}/{EPOCHS}] | Loss Treino: {avg_loss:.4f} | Acurácia Validação: {accuracy:.2f}%")

    print("\nTreinamento finalizado.")
    os.makedirs(MODELS_DIR, exist_ok=True)
    torch.save(model.state_dict(), MODEL_PATH)
    print(f"Modelo salvo em: {MODEL_PATH}")

# =============================================================================
# SEÇÃO 5: PREVISÃO (de 03_predict.py)
# =============================================================================
def analisar_imagem(caminho_imagem):
    print("\n--- ETAPA 3: Fazendo uma Previsão de Exemplo ---")

    if not os.path.exists(MODEL_PATH):
        print(f"ERRO: Modelo '{MODEL_PATH}' não encontrado para fazer a previsão.")
        return
    if not os.path.exists(caminho_imagem):
        print(f"ERRO: Imagem de teste '{caminho_imagem}' não encontrada.")
        return

    # As classes são inferidas a partir dos nomes das pastas de treino
    classes_do_treino = sorted(os.listdir(os.path.join(PROCESSED_DATA_PATH, 'train')))
    
    model = SpectrogramCNN(num_classes=len(classes_do_treino)).to(DEVICE)
    model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
    model.eval()

    transform = transforms.Compose([
        transforms.Grayscale(),
        transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])
    
    imagem = Image.open(caminho_imagem)
    imagem_tensor = transform(imagem).unsqueeze(0).to(DEVICE)

    with torch.no_grad():
        output = model(imagem_tensor)
        _, predicted_idx = torch.max(output.data, 1)
        predicted_class = classes_do_treino[predicted_idx.item()]
        
    print(f"Analisando: '{caminho_imagem}'")
    print(f"Resultado: A imagem foi classificada como '{predicted_class}'.")

# =============================================================================
# PONTO DE ENTRADA PRINCIPAL
# =============================================================================
if __name__ == '__main__':
    # Etapa 1
    dados_prontos = process_all_audio()
    
    # Se os dados foram preparados com sucesso, continua para o treino
    if dados_prontos:
        # Etapa 2
        train_model()
        
        # Etapa 3 - Exemplo de previsão
        # CRIE UMA IMAGEM DE TESTE E COLOQUE O CAMINHO AQUI
        IMAGEM_PARA_TESTAR = "caminho/para/sua/imagem_de_teste.png" 
        analisar_imagem(IMAGEM_PARA_TESTAR)