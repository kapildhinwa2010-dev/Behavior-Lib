import pytest
import torch
from behavior_lib import BehaviorLib, create_behavior_lib

class TestBehaviorLib:
    def test_init(self):
        m = BehaviorLib(dim=256, hidden_dim=512)
        assert m.dim == 256
    
    def test_forward(self):
        m = BehaviorLib(dim=256)
        x = torch.randn(32, 256)
        assert m(x).shape == (32, 256)
    
    def test_factory(self):
        m = create_behavior_lib()
        assert isinstance(m, BehaviorLib)

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
