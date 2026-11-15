# Behavior-Lib

[![CI](https://github.com/kapildhinwa2010-dev/Behavior-Lib/actions/workflows/ci.yml/badge.svg)](https://github.com/kapildhinwa2010-dev/Behavior-Lib/actions/workflows/ci.yml)
[![CodeQL](https://github.com/kapildhinwa2010-dev/Behavior-Lib/actions/workflows/codeql.yml/badge.svg)](https://github.com/kapildhinwa2010-dev/Behavior-Lib/actions/workflows/codeql.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch 2.0+](https://img.shields.io/badge/pytorch-2.0+-red.svg)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

**Behavior library**

Professional implementation of Behavior-Lib for research and production use.

## Installation

```bash
pip install Behavior-Lib
```

## Usage

```python
import torch
from behavior_lib import BehaviorLib

module = BehaviorLib(dim=256, hidden_dim=512)
output = module(torch.randn(32, 256))
```

## License

MIT License
