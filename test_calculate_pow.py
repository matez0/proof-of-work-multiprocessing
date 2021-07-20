from hashlib import sha1
from time import perf_counter

import pytest

from pow_calculator import calculate_pow


test_data = [
    'NMJDwDLSGwiJRcdOiwyeyFpZSbnaFSZPJCoFNvrqFFRjjxGxufKEDKmtBrSULHCe',
    'bCTNzBWdmuzjrOsOHNwVMUoiKqreBZoXGAZOyDoHGaZtGFPArQeBNNSAOHphughq',
    'mmhxAuitDefBRtJXunJMbKyYUkacTLbQmtUklVrfxPJCQzhtqSAdBhxARDYbluiV',
    'xOLhHSZorlXVEIAEpDMEkiFyuZywXnDhHjSnIBsyMlwumDyLuUxwMlmpXajAoskT',
    'XDNLtzVOXjFXvAhJUguJuXThSALSrmBUEHyWbPLteLNnWupNsmGjjOSXhhyDXHNX',
    'yHYPpeDoZtausMLaqAhBKzkNXQOgTJZZFNFSLAyhVRwDKaLuUvCeXSgVqjMPUFSr',
    'YczpCSqUpliNTBcWSlsOLoDvBklPomLZidKGAfEFIRfqZIpQKdQTzfnyVkVWqzhc',
    'FgUcLPSDNSUpjsaxRposXIkPMgVtwOsURAoMNmHRSbgjUonPPKQpPivhvMldKwmw',
    'jucevuUgAvZJRCBDvImuBnnCptTvSnbAvUODWSKEPNhzqJByfGyqmPeIbGLrMAFG',
    'NPysmhIldJEvldCQdpqHNuuhWEjUGMuKiRnOIsxYnbIEZTlAMbnrldreGSUqQRpr',
]


@pytest.mark.parametrize("input_data", test_data)
def test_calculate_pow_returns_suffix_proper_for_making_hash_with_leading_zeros(input_data):
    difficulty = 6

    time = perf_counter()
    suffix = calculate_pow(input_data, difficulty)
    time = perf_counter() - time

    checksum = sha1((input_data + suffix).encode()).hexdigest()

    print(f'{time:.1f} {suffix} {checksum}')

    assert checksum.startswith('0' * difficulty)
