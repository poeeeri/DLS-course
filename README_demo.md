# Демонстрация nn.Module.to()

**Студент:** Доржиева Пурбо-Суруна  
**Библиотека:** PyTorch `2.14.1`  
**Репозиторий исходников:** https://github.com/pytorch/pytorch  
**Исследуемый исходник:** https://github.com/pytorch/pytorch/blob/v2.14.1/torch/nn/modules/module.py

## Запуск

Из корня проекта с `.venv`:

```powershell
.\.venv\Scripts\python.exe -m pip install torch==2.14.1 --index-url https://download.pytorch.org/whl/cpu
.\.venv\Scripts\python.exe demo_to.py
```

`demo_to.py` для cpu. `float32` -> `float64` для проверки того же пути `Module.to()` / `_apply()` без CUDA.