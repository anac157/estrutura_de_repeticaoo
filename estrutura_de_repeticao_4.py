pais_A_habitantes, pais_A_crecimento = 80_000,  3
pais_B_habitantes, pais_B_crecimento = 200_000, 1.5

anos = 0
while pais_A_habitantes < pais_B_habitantes:
    anos += 1
    pais_A_habitantes = pais_A_habitantes / pais_A_crecimento * 100 + pais_A_habitantes
    pais_B_habitantes = pais_B_habitantes / pais_B_crecimento * 100 + pais_B_habitantes


print(f'Daqui {anos}.')
