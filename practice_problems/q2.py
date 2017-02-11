def findSecondHighest(arr):
	return max(arr),arr.index(max(arr))
	
def getMaxVolume(heights,distances,depth,columnWidth):	
	maxHeight = max(heights)
	ind_max = heights.index(maxHeight)
	gross_vol = []

	while (ind_max > 0):
		snd_hgt_l,ind_snd_hgt_l = findSecondHighest(heights[:ind_max])
		if snd_hgt_l == None:
			break

		sum = 0
		for i in range(ind_snd_hgt_l,ind_max):
			sum += distances[i]
		vol_l = sum*snd_hgt_l*depth

		gross_vol.append(vol_l)

		maxHeight = snd_hgt_l
		ind_max = ind_snd_hgt_l

	while ind_max < len(heights):
		snd_hgt_r,ind_snd_hgt_r = findSecondHighest(heights[ind_max:])
		if snd_hgt_r == None:
			break
		ind_snd_hgt_r += ind_max

		sum = 0
		for i in range(ind_max,ind_snd_hgt_r):
			sum += distances[i]
		vol_r = sum*snd_hgt_r*depth

		gross_vol.append(vol_r)

		maxHeight = snd_hgt_r
		ind_max = ind_snd_hgt_r

	return max(gross_vol)	
	