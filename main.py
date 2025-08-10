import sys
import io
from sistema_llantera_db import SistemaLlantera

# Configurar la salida estándar para usar UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main():
    print("🔧 Iniciando Clamatin")
    print("=" * 30)
    sistema = SistemaLlantera()
    sistema.run()

if _name_ == '_main_':
    main()