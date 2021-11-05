import json
import hashlib
method = 'default'

def whichServer(method):
    if method == 'SHA256':
        path = 'Authentication\JSON_SHA256.JSON'

    return path


def manipulation(method, tipo, save_json):

    path = whichServer(method)

    if tipo == 'r':
        f = open(path, 'r')
        JSON = json.load(f)
        f.close()
        return JSON

    if tipo == 'w':
        f = open(path, 'w')
        json.dump(save_json, f)
        f.close()
        




def authentication(user, password, method):
    json_data = manipulation(method, 'r', '')
    
    #CHECK DE CORRESPONDENCIA NO BD(json)
    try:
        if json_data[user]:
            check = 'Ok'
    except: 
        return False        

    
    
    #FUNÇÕES DE CHECK CRIPTO/HASH DE ACORDO COM METHOD

    if method == 'SHA256':
        if hashlib.sha256(password.encode()).hexdigest() == json_data[user]:
            return True
        else:
            return False


    #CHAVE ASSIMETRICA

    




def registration(user, password):
    
    #SHA256
    json_data = manipulation('SHA256', 'r', '')
    json_data[user] = hashlib.sha256(password.encode()).hexdigest()
    manipulation('SHA256', 'w', json_data)