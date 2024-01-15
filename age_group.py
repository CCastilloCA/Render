def get_age_group(age):
    """
    Devuelve el grupo de edad basado en la edad en años dentro del intervalo 0..150,
    de lo contrario, devuelve 'desconocido'.
    """
    if 0 <= age <= 150:
        if age <= 14:
            return 'infancia'
        elif age <= 24:
            return 'juventud'
        elif age <= 64:
            return 'adulto'
        else:
            return 'vejez'
    else:
        return 'desconocido'

def test_get_age_group():
    """Prueba unitaria para get_age_group"""
    assert get_age_group(-1) == 'desconocido'
    assert get_age_group(0) == 'infancia'
    assert get_age_group(14) == 'infancia'
    assert get_age_group(15) == 'juventud'
    assert get_age_group(24) == 'juventud'
    assert get_age_group(25) == 'adulto'
    assert get_age_group(64) == 'adulto'
    assert get_age_group(65) == 'vejez'
    assert get_age_group(80) == 'vejez'
    assert get_age_group(150) == 'desconocido'

# Esta parte ejecuta las pruebas unitarias con pytest.
if __name__ == "__main__":
    import pytest
    pytest.main(['-rA'])
 