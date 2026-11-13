
import sys
import torch

print("Python Version:", sys.version)
print("Python Executable:", sys.executable)
print("PyTorch Version:", torch.__version__)
print("CUDA Version:", torch.version.cuda)
print("GPU Available:", torch.cuda.is_available())

