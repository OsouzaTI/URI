positivos = 0
n_pos = []
media = 0
for i in range(6):
	n = float(input())
	if n > 0:
		positivos += 1
		n_pos.append(n)
for i in range(len(n_pos)):
	media = media + n_pos[i]
media = media/positivos
print('%i valores positivos\n%.1f'%(positivos,media))
