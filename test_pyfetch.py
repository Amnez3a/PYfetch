from PYfetch import get_cpu_model

def test_get_cpu_model():
    result = get_cpu_model()
    assert isinstance(result, str) 
    assert result.strip() != "" 