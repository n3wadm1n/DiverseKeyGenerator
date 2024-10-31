#!/usr/bin/python3
####################
################
### n3wadm1n #####
### Euribot  #####
#####################
import random, string, argparse, sys, base64

b64_art = "4paR4paI4paA4paE4paR4paA4paI4paA4paR4paI4paR4paI4paR4paI4paA4paA4paR4paI4paA4paE4paR4paI4paA4paA4paR4paI4paA4paAICAgICAgICAK4paR4paI4paR4paI4paR4paR4paI4paR4paR4paA4paE4paA4paR4paI4paA4paA4paR4paI4paA4paE4paR4paA4paA4paI4paR4paI4paA4paAICAgICAgICAK4paR4paA4paA4paR4paR4paA4paA4paA4paR4paR4paA4paR4paR4paA4paA4paA4paR4paA4paR4paA4paR4paA4paA4paA4paR4paA4paA4paAICAgICAgICAK4paR4paI4paR4paI4paR4paI4paA4paA4paR4paI4paR4paIICAgICAgICAgICAgICAgICAgICAgICAgCuKWkeKWiOKWgOKWhOKWkeKWiOKWgOKWgOKWkeKWkeKWiOKWkSAgICAgICAgICAgICAgICAgICAgICAgIArilpHiloDilpHiloDilpHiloDiloDiloDilpHilpHiloDilpEgICAgICAgICAgICAgICAgICAgICAgICAK4paR4paI4paA4paA4paR4paI4paA4paA4paR4paI4paA4paI4paR4paI4paA4paA4paR4paI4paA4paE4paR4paI4paA4paI4paR4paA4paI4paA4paR4paI4paA4paI4paR4paI4paA4paECuKWkeKWiOKWkeKWiOKWkeKWiOKWgOKWgOKWkeKWiOKWkeKWiOKWkeKWiOKWgOKWgOKWkeKWiOKWgOKWhOKWkeKWiOKWgOKWiOKWkeKWkeKWiOKWkeKWkeKWiOKWkeKWiOKWkeKWiOKWgOKWhArilpHiloDiloDiloDilpHiloDiloDiloDilpHiloDilpHiloDilpHiloDiloDiloDilpHiloDilpHiloDilpHiloDilpHiloDilpHilpHiloDilpHilpHiloDiloDiloDilpHiloDilpHiloAK"
b64_bt = b64_art.encode('utf-8')
as_bt = base64.b64decode(b64_bt)
as_art = as_bt.decode('utf-8')
print(as_art)
print("\n -- - -- - -- - --\n")

min_pswd_le = 15

def grt_pswd(ma_count, mi_count, dg_count, es_count):
    special_characters = "我你他她是有这那吗在不好大小爱去来知道ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅜㅝㅞㅟㅠㅡㅣㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎアイウエオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂツヅテデトナニヌネノハバヒビフブヘベホボマミムメモヤユヨラリルレロワヲンぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢつづてでとななにぬねのはばひびふぶへべほぼまみむめもやゆよらりるれろわをんАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯçñäàáâãéêëèíìïîóòôõöúùûüÿý!@#$%&*()_+=<>?/[]{}|¹²³£¢¬-§ª^°"
    
    ma_part = random.choices(string.ascii_uppercase, k=ma_count)
    mi_part = random.choices(string.ascii_lowercase, k=mi_count)
    dg_part = random.choices(string.digits, k=dg_count)
    es_part = random.choices(special_characters, k=es_count)
    
    pswd = ma_part + mi_part + dg_part + es_part
    
    random.shuffle(pswd)
    
    return ''.join(pswd)

def grt_ra_pswd(length):
    all_characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + "我你他她是有这那吗在不好大小爱去来知道ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅜㅝㅞㅟㅠㅡㅣㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎアイウエオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂツヅテデトナニヌネノハバヒビフブヘベホボマミムメモヤユヨラリルレロワヲンぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢつづてでとななにぬねのはばひびふぶへべほぼまみむめもやゆよらりるれろわをんАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯçñäàáâãéêëèíìïîóòôõöúùûüÿý!@#$%&*()_+=<>?/[]{}|¹²³£¢¬-§ª^°"
    
    password = random.choices(all_characters, k=length)
    return ''.join(password)

def main():
    parser = argparse.ArgumentParser(description="Strong and complex password generator.")
    
    parser.add_argument("--ma", type=int, default=2, help="Number of uppercase letters in the password")
    parser.add_argument("--mi", type=int, default=4, help="Number of lowercase letters in the password")
    parser.add_argument("--nu", type=int, default=2, help="Number of digits in the password")
    parser.add_argument("--es", type=int, default=2, help="Number of special characters in the password")
    
    parser.add_argument("--ra", type=int, help="Generate a password with a random distribution of characters with the specified total length")
    
    args = parser.parse_args()
    
    if args.ra is not None:
        if args.ra < min_pswd_le:
            print(f"Error: The length of the password ({args.ra}) is less than the minimum required ({min_pswd_le}).")
            sys.exit(1)
        pswd = grt_ra_pswd(args.ra)
    
    else:
        total_length = args.ma + args.mi + args.nu + args.es
        
        if total_length < min_pswd_le:
            print(f"Error: The total length of the password ({total_length}) is less than the minimum required ({min_pswd_le}).")
            print("Please insert the values for --ma, --mi, --nu and --es to meet the minimum length.")
            sys.exit(1)
        
        pswd = grt_pswd(args.ma, args.mi, args.nu, args.es)
    
    print("Generated password:\n", pswd)

if __name__ == "__main__":
    main()
