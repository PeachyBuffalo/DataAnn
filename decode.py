def mapping(lines):
    num_map = {}
    for line in lines:
        num, word = line.strip().split(' ', 1)
        num_map[int(num)] = word
    return num_map

def decode(text_file):
    with open(text_file, 'r') as file:
        lines = file.readlines()
    
    num_map = mapping(lines)
    
    total_numbers = len(num_map)
    pyramid_height = 1
    while (pyramid_height * (pyramid_height + 1)) // 2 <= total_numbers:
        pyramid_height += 1
    pyramid_height -= 1 
    key_numbers = []
    for i in range(1, pyramid_height + 1):
        key_number = (i * (i + 1)) // 2
        key_numbers.append(key_number)
    
    hidden_message = ' '.join([num_map[number] for number in key_numbers])
    
    return hidden_message

decoded_message = decode('coding_qual_input.txt')
print(decoded_message)
