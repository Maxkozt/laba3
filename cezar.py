def cezar(text, krok):
        alf = "абвгґдуєжзиіїйкльмншщпрстуфхцчшщьюяабвгґдуєжзиіїйкльмншщпрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯabsdefghijklmnopqrstuvwxyzabsdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWABCDEFGHIJKLMNOPQRSTUVW1234567890"
        step = krok 
        message = text 
        result = "" 
        for i in message:
            cell = alf.find(i) 
            new_cell = cell + step 
            if i in alf:
                result += alf[new_cell]
            else:
                result += i
        return result


print(cezar(input(), 1))

