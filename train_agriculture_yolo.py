#Materi 2: Bridging Global Infrastructure to Address Local Challenge with HPC
import torch
from ultralytics import YOLO

# Studi Kasus: Deteksi penyakit tanaman/pemetaan lahan (Adaptasi konsep DigiFarm)
def main():
    print("=== MEMULAI TRAINING: YOLOv11 untuk Pemetaan Lahan Pertanian ===")
    
    # Memeriksa ketersediaan GPU/HPC untuk akselerasi
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"Menggunakan komputasi: {device}")


    model = YOLO('yolov11n.yaml') 


    results = model.train(
        data='local_agriculture_dataset.yaml',
        epochs=100,
        imgsz=640,
        device=device,
        project='HPC_Agriculture_Mapping',
        name='yolo_agri_model'
    )
    
    print("Training selesai. Model siap digunakan untuk deteksi presisi.")

if __name__ == '__main__':
    main()
    