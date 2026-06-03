from pyneofetch import *

def test_get_cpu_model():
    result = get_cpu_model()
    assert isinstance(result, str) 
    assert result.strip() != "" 

def test_get_cpu_temp():
    result = get_cpu_temp()
    assert isinstance(result, str) 
    assert result.strip() != "N/A"

def test_get_package_count():
    result = get_package_count()
    assert isinstance(result, str) 
    assert result.strip() != "Unknown"

def test_get_pc_info():
    result = pc_info()
    assert isinstance(result, dict) 
    assert "OS" in result
    assert "Kernel" in result
    assert "Uptime" in result
    assert "Packages" in result
    assert "Shell" in result
    assert "Resolution" in result
    assert "DE" in result
    assert "WM" in result
    assert "CPU" in result
    assert "GPU" in result
    assert "Memory" in result

def test_user_info():
    result = user_info()
    assert isinstance(result, list) 
    assert len(result) == 2 
    assert result[0].startswith("User:") 
    assert result[1].startswith("Home:")

def test_desktop_info():
    result = desktop_info()
    assert isinstance(result, list) 
    assert len(result) == 4 
    assert result[0].startswith("Shell:") 
    assert result[1].startswith("WM/DE:") 
    assert result[2].startswith("Term:") 
    assert result[3].startswith("Env:")

def test_other_info():
    result = other_info()
    assert isinstance(result, list) 
    assert len(result) == 1 
    assert result[0].startswith("Python:")

def test_build_info_lines():
    result = build_info_lines()
    assert isinstance(result, list) 
    assert len(result) > 0 
    assert any(line.startswith("[ ") and line.endswith(" ]") for line in result)

def test_render():
    art_str = "Test Art"
    info_lines = ["Line 1", "Line 2", "Line 3"]
    result = render(art_str, info_lines)
    assert isinstance(result, str) 
    assert art_str in result 
    for line in info_lines:
        assert line in result

def test_main():
    result = main()
    assert isinstance(result, str) 
    assert "Host:" in result 
    assert "OS:" in result 
    assert "Kernel:" in result 
    assert "CPU:" in result 
    assert "GPU:" in result 
    assert "RAM:" in result 
    assert "Disk:" in result 
    assert "Packages:" in result 
    assert "Uptime:" in result 
    assert "User:" in result 
    assert "Home:" in result 
    assert "Shell:" in result 
    assert "WM/DE:" in result 
    assert "Term:" in result 
    assert "Env:" in result 
    assert "Python:" in result