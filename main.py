

# Variant 1
# Small exponent attack variant 1
TEST_CASE = (
    [ # C_VALUES
        0x9f18cb5a10b43cb08f799bb599e6f1efb981c9a5cd352793715c5204e879ef37,
        0x4228bc1401f6deb12f8235f67779d5f4429b76c42d176b17a8d636a173f1364f,
        0x42ff76fd7459f6fb63bffb9380467b6822fa1ee7d6843c06d55b75f01776c9ce,
    ],
    [ # N_VALUES
        0xD7E0B1B02BCE1C6E2213595E70350EFD3B45980ACC354447E43A31277C775A25,
        0xABDDDA209D6C7583D4D48DE609C7DAAA13ACC17222765058D0BA5D85A689EB87,
        0xB85BB9166C83050778CD2EE9AD9BBEB1826387952C36A1887CAE5CC1028C44F9,
    ],
    3 # E_VALUE
)

TASK = (
    [ # C_VALUES
        0x530d7fe6405732669c3c6d25255a70980036e52c38414f66732a8c9cd73df7e1a4cb9280ec7316666bfcc24b1d2333cc142971cf7e96e2e1b30894d12ff0181a174cf702d6b7c3d84a6a9eed9af65ca0aeff28ce14b324d1b6178d3732e359804c4d2da1197a2df724040ed87c192aa61acfaee0aeda60085e6ba43be9461712,
        0xa8ed69e9b6f909a9e9aefa7fdffce684b5aa8da98da3b9ecf6606ed779b3a81a57d424082af9bebcd519a02b9ac0746ba66777e7e549b5d05a9ab5b7837eae11626336fb9e1b48c800d62fa0932d918b18f5de769d2ba7323314fdda7b7be6a1b2c42ccb8050c5c825e880023d580d8489840e152866b2899fc266cae7721cac,
        0x75e9a42fea1c228363764feac2af7f2cd64279b9e74a0a8fb544569b23554249451aae168adead55ce20b82d81a5b2e7a877cf728fe3d2cf3a4ab394fabd517b133254a9ba8812b39ae6407d1c2e69a1f94ce2cb41c1b347c099f43d53e339074d6d2151d2341582f2b41cbf59d7ed86c8458793cccda84d758ca0fd23e8bfe1,
        0x9833ae11ced83cf8b91e2608452a01f0652a4dc65ffe16859471bc24bd72bec8e6ae3d6695fcf0078fff0c1bdc0cd51437482664dab7d6f77aad48ca168b02c5db4519afed15c70bb9fd59c10e0fe5275f3274ac0de2ab5a62100c5a8c81b827745f8cf0dab765d3b2c55cdf69295b476e54016184ca50dde59a6116a8eafc32,
        0x43314bf6c436f1f90e4742adf078623ca5e77f722d203b470ed150862b069542b499a74874f088368c1da8756d27fa54632e6e20ac35d9f3b68b33aa787cd9a29b6bb0fae24f4ecd584add2fd13feda674b31e3d8af9b4107d0c40ab10801a3b8c9a28ba92ffecfadfe62801bfd7366c2bb53b006a95aea133107da57e52bed5,
    ],
    [ # N_VALUES
        0xC5BC5A160E989EF4DD2E82470B9C886E237AF09C40CCEF73AD395D643E41836267CB51E07C28AF3887818DE08FD880BC828560686E8350DEA77859C698EA7A3B29A614FF587F3457102B4E093A7488EEBDE3CD15CF6514A8ED2AFADD991F1F661FD8F4BD0458853058F3F560566F2A75AD8BC0C631F58A41DD01293A0620BC43,
        0xC1F1DEE2DA43997D0154FFF328EB41C6B488F9B5FDBFA23DFFFC0506D7A1E3E525E0780B98647265B55C596E39E6E31A9709F4665A310CBF645CAD54A31CCDF506D64DDDF5AF32D2A8AB6FA4E21073135ACBBE50F909B22538A8AAD253FAB24EC89E34653F133699D69BE10B1D8E25E4A304D874B972552F0FEF55C4293CEB45,
        0x99F6D2706B8B6BFA767EF8DABCEEC14093540410E5A842BF8082027CAA561FFC98CB846942E0135E180CBE9F30DAB667EC9494F5CDDFE526C4A8174B2111CDADFA37B54F2923C951D99507F5EEB752C2AA9DAF3FCFF104C6BDE32178C21921A48AEE71C558D3DE2C8A00B68221D73819162FD195AC8C7CAAD77463B5F3C5E525,
        0xA6E1CD5F24984CC77B986631F655B8AE940A22B6ABA0C3B1B6A38FE2D742D61ECCB095E56CC5B034EEF664E9F1D80C592A866A9FB1887F8AF7167660C696902743F64EF482D993D70ACC8EF0CBA80C3738EA6100729177E235FE7879133CF6B8A658B2B1ACFB615B1C5F618E67A3D3CD06E5E878E59644CECA952C1DAEF58F0B,
        0xC348FFF9D07BACE864DA0E060AC2062B92538F10D5D4A972CA0BA0CBC535ACBDB23B2297EE8DE0CC818B60CD93F8AB8BF2D6B34863305F32CD75FB7D3C49460A7A9FCDFE3DEF1FC0AB2080015059660F8D2501A51E96E61F10CEE4A661CEF7F9A6B25EFFBC5C05700AF81DB059162047D7AF3A936B7D50606EEF4DB48346263F,
    ],
    5 # E_VALUE
)

# Use Chinese remainder theorem to find a solution of the system:
#       x_1 = a_1 (mod n_1)
#       x_2 = a_2 (mod n_2)
#       ...
#       x_k = a_k (mod n_k)
# in form x mod N, where N = n_1  * n_2 * ... * n_k
def chinese_remainder_theorem(a_values: list, n_values: list) -> int:
    k = len(a_values)
    if len(n_values) != k:
        raise ValueError("Paramethers must be of the same size.")
    
    N = 1
    for n in n_values:
        N *= n

    x = 0
    for a, n in zip(a_values, n_values):
        M_i = N // n
        N_i = pow(M_i, -1, n)
        x += a * M_i * N_i
    
    return x % N

def main():
    pass

if __name__ == "__main__":
    main()

