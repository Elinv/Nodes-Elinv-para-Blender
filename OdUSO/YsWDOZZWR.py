import bpy, os, pathlib, platform
from datetime import datetime
import uuid
import subprocess
import sys
import requests
import socket
claves = [
    "#~bd68cd21-10cd-48dc-b97e-1d5e4b1b95d9 {#~2012-11-23E9D22B4-A1B4-4B09-9F5D-9B5140C1F22F} ",
    "#~{E62F4180-#~2019-12-128E1A2-4851-BD69-19411D459940} #~d6a611ee8c7a1c872c710f77#~2020-4-18#~d6a611ee8c7a1c872c710f77 #~d6a611ee8c7a1c872c710f77#~2021-2-2#~d6a611ee8c7a1c872c710f77",
    "#~c7d0695e-bc35-4204-8bcc-#~2023-2-128604f06b29b58 c7d0695e-bc35-4204-8bcc-604f06b29b58",
    "#~857430ef-610f-41ea-#~2024-2-15ae05-988d8875924f",
    "#~82fcb54c-213d-#~2024-2-2844b2-8ac5-e2bcb11113cd",
    "#~d6a611ee8c7a1c872c710f77#~2024-2-28#~d6a611ee8c7a1c872c710f77",
    "#~bd68cd21-10cd-48dc-b97e-1d5e4b1b95d9 {#~2012-11-23E9D22B4-A1B4-4B09-9F5D-9B5140C1F22F} ",
    "#~{E62F4180-#~2019-12-128E1A2-4851-BD69-19411D459940} #~d6a611ee8c7a1c872c710f77#~2020-4-18#~d6a611ee8c7a1c872c710f77 #~d6a611ee8c7a1c872c710f77#~2021-2-2#~d6a611ee8c7a1c872c710f77",
    "#~c7d0695e-bc35-4204-8bcc-#~2023-2-128604f06b29b58 c7d0695e-bc35-4204-8bcc-604f06b29b58",
    "#~857430ef-610f-41ea-#~2024-2-15ae05-988d8875924f",
    "#~82fcb54c-213d-#~2024-2-2844b2-8ac5-e2bcb11113cd",
    "#~d6a611ee8c7a1c872c710f77#~2024-2-28#~d6a611ee8c7a1c872c710f77",
    "#~857430ef-610f-41ea-#~2024-2-15ae05-988d8875924f",
    "#~82fcb54c-213d-#~2024-2-2844b2-8ac5-e2bcb11113cd",
    "#~d6a611ee8c7a1c872c710f77#~2020-4-18#~d6a611ee8c7a1c872c710f77 #~d6a611ee8c7a1c872c710f77#~2021-2-2#~d6a611ee8c7a1c872c710f77",
    "#~c7d0695e-bc35-4204-8bcc-#~2023-2-128604f06b29b58 c7d0695e-bc35-4204-8bcc-604f06b29b58",
    "#~bd68cd21-10cd-48dc-b97e-1d5e4b1b95d9 {#~2012-11-23E9D22B4-A1B4-4B09-9F5D-9B5140C1F22F}",
    "#~d6a611ee8c7a1c872c710f77#~2020-4-18#~d6a611ee8c7a1c872c710f77 #~d6a611ee8c7a1c872c710f77#~2021-2-2#~d6a611ee8c7a1c872c710f77",
    "#~c7d0695e-bc35-4204-8bcc-#~2023-2-128604f06b29b58 c7d0695e-bc35-4204-8bcc-604f06b29b58",
    "#~82fcb54c-213d-#~2024-2-2844b2-8ac5-e2bcb11113cd",
    "#~d6a611ee8c7a1c872c710f77#~2020-4-18#~d6a611ee8c7a1c872c710f77",
    "#~d6a611ee8c7a1c872c710f77#~2024-2-28#~d6a611ee8c7a1c872c710f77",
]
k1 = ""
k2 = ""
k3 = ""
f1 = ""
f2 = ""
f3 = ""
archivos = [
    "ñkyxpukxJrbpv&qbt",
    "kvbyexwxmni1k&qbt",
    "xwxdkñ&qbt",
    "rki&qbt",
]
mensajes = [
    "Sxdp ekrxby ok trzklp jp mpozmpoc", 
    "Ikrxby ok trzklp",
    "Ñrcirpñp p nzvv",
    "Ikrxbcy nzvv pmdbepop",
]
def ezIrBxgQS():
    if platform.system() == "Linux":
        dirworkVers = bpy.utils.resource_path('LOCAL')
        dirworkVersScr = bpy.utils.resource_path('LOCAL') + "/scripts"
        dirworkVersScrAdd = bpy.utils.resource_path('LOCAL') + "/scripts/addons"
        dirworkVersMod = bpy.utils.resource_path('LOCAL') + "/scripts/modules"
    elif platform.system() == "Windows":
        dirworkVers = bpy.utils.resource_path('USER')
        dirworkVersScr = bpy.utils.resource_path('USER') + "\\scripts"
        dirworkVersScrAdd = bpy.utils.resource_path('USER') + "\\scripts\\addons"
        dirworkVersMod = bpy.utils.resource_path('USER') + "\\scripts"
    arch1 = BtheMweEE(archivos[0])
    arch2 = BtheMweEE(archivos[1])
    arch3 = BtheMweEE(archivos[2])
    full_pathArch1 = os.path.join(dirworkVersScr, arch1)
    full_pathArch2 = os.path.join(dirworkVersScrAdd, arch2)
    full_pathArch3 = os.path.join(dirworkVersMod, arch3)
    print(full_pathArch1)
    print(full_pathArch2)
    print(full_pathArch3)
    return full_pathArch1, full_pathArch2, full_pathArch3
def lzHcXaWfj(msg):
    Chars_x="abcdefghijklmnñopqsrtuvwyxzABCDEFGHIJKLMNÑOPQSRTUVWYXZ0123456789,.;/()? "
    Chars_y="plmoknijbuhvñygctfxrdzeswaqQAZWSXEDCRFVTGBYÑHNUJMIKOLP7531902468(&;%.?) "
    msg_cifrado=""
    for x in msg:
        for n  in range(len(Chars_x)):
            if x==Chars_x[n]:
                msg_cifrado+=Chars_y[n]
    return msg_cifrado
def GfiAtGfzT(self, context):
    scene = context.scene
    arch4 = BtheMweEE(archivos[3])
    if os.path.isfile(arch4):
        try:
            dateKey = vpAeDcDmy(arch4)
            x = dateKey.split("#~")
            uuidKeyDesarrollador = x[-1]
            uuid = TbCeBGqVI()
            if platform.system() == "Windows":
                uuid = uuid.replace("-", "")
            uuidKeyUser = gkcd(uuid)
            if uuidKeyDesarrollador == uuidKeyUser:
                msg = BtheMweEE(mensajes[3])
                self.report({'INFO'}, msg)
                scene.keyActivation = uuidKeyDesarrollador
                scene.inpUserName = "**************"
                scene.inpPassword = "**************"
                return -1
        except:
            return 1
    return 1
def dev(clave):
    totKey = len(clave)
    dig,alfa,sum = 0,0,totKey
    for x in clave:
        if x.isdigit()==True:
            dig += 1
            if int(x) != 0:
                sum *= int(x)
        else:
            alfa += 1
    return clave,dig,alfa,sum
def strk(clave,dig,alfa,sum):
    clave = str(len(clave)) + "" + str(dig) + "" + str(alfa) + "" + str(sum)
    return clave
def rkf(clave):
    res = ""
    for idx, x in enumerate(clave):
        if idx % 4 == 0 and idx != 0:
            res += "-"
            res += x
        else:
            res += x
    return res
def gkcd(clave):
    clave,dig,alfa,sum = dev(clave)
    clave = strk(clave,dig,alfa,sum)
    return rkf(clave)
def vpAeDcDmy(arch):
    with open(arch, 'r') as f:
        last_line = f.readlines()[-1]   
        return last_line 
def CkpJBFXxf(arch, data):
    f = open(arch, "a+")
    for x in claves:
        f.write("\n" + x)
    current_dateTime = datetime.now()
    hoy = str(current_dateTime.year) + "-" + str(current_dateTime.month) + "-" + str(current_dateTime.day)
    f.write(str("\n"))
    f.write(str("#~"+data))
    f.write(str("#~"+hoy))
    f.write(str("#~"+data))
    f.close()
def run(cmd):
    try:
        return subprocess.run(cmd, shell=True, capture_output=True, check=True, encoding="utf-8") \
                         .stdout \
                         .strip()
    except:
        return None
def TbCeBGqVI():
    if sys.platform == 'darwin':
        return run(
            "ioreg -d2 -c IOPlatformExpertDevice | awk -F\\\" '/IOPlatformUUID/{print $(NF-1)}'",
        )
    if sys.platform == 'win32' or sys.platform == 'cygwin' or sys.platform == 'msys':
        return run('wmic csproduct get uuid').split('\n')[2] \
                                             .strip()
    if sys.platform.startswith('linux'):
        return run('cat /var/lib/dbus/machine-id') or \
            run('cat /etc/machine-id')
    if sys.platform.startswith('openbsd') or sys.platform.startswith('freebsd'):
        return run('cat /etc/hostid') or \
            run('kenv -q smbios.system.uuid')
def klrfOIXAc(self):
    dateInstalacion = "" #datetime.strptime("2021-12-25", "%Y-%m-%d")
    arch1, arch2, arch3 = ezIrBxgQS()
    if os.path.isfile(arch1):    
        dateKey = vpAeDcDmy(arch1)
        x = dateKey.split("#~")
        dateInstalacion = datetime.strptime(x[2], "%Y-%m-%d")
    current_dateTime = datetime.now()
    hoy = str(current_dateTime.year) + "-" + str(current_dateTime.month) + "-" + str(current_dateTime.day)
    dateActual = datetime.strptime(hoy, "%Y-%m-%d")
    diferencia = dateActual - dateInstalacion
    dias = BtheMweEE("57")
    if (diferencia.days > int(dias)):
        msg = BtheMweEE(mensajes[0])
        self.report({'INFO'}, msg)        
        return [msg, 0, diferencia.days, int(dias)]
    else:
        msg = BtheMweEE(mensajes[1])
        self.report({'INFO'}, msg)        
        return [msg, 1, diferencia.days, int(dias)]
def BtheMweEE(msg):
    Chars_y="abcdefghijklmnñopqsrtuvwyxzABCDEFGHIJKLMNÑOPQSRTUVWYXZ0123456789,.;/()? "
    Chars_x="plmoknijbuhvñygctfxrdzeswaqQAZWSXEDCRFVTGBYÑHNUJMIKOLP7531902468(&;%.?) "
    msg_cifrado=""
    for x in msg:
        for n  in range(len(Chars_x)):
            if x==Chars_x[n]:
                msg_cifrado+=Chars_y[n]
    return msg_cifrado
def yiirdFDlL(self):
    idTbCeBGqVI = TbCeBGqVI()
    arch1, arch2, arch3 = ezIrBxgQS()
    print("Arch3 -> " + arch3)
    global k1
    global k2
    global k3
    global f1
    global f2
    global f3    
    if os.path.isfile(arch1):
        try:
            dateKey = vpAeDcDmy(arch1)
            x = dateKey.split("#~")
            f1 = x[2]
            k1 = x[-1]
        except:
            print("Excepción Trial")
    else:
        print("Excepción Trial")
    if os.path.isfile(arch2):
        try:
            dateKey = vpAeDcDmy(arch2)
            x = dateKey.split("#~")
            f2 = x[2]
            k2 = x[-1]
        except:
            print("Excepción Trial")
    if os.path.isfile(arch3):
        try:
            dateKey = vpAeDcDmy(arch3)
            x = dateKey.split("#~")
            f3 = x[2]
            k3 = x[-1]
        except:
            print("Excepción Trial")
    else:
        print("Excepción Trial")
    print(f1 + " f1 " + f2 + " f2 y " + f3 + " f3 ")
    if f1 != "" and f2 != "" and f3 != "" and k1 != "" and k2 != "" and  k3 != "" and f1 == f2 and f2 == f3 and k1 == k2 and k2 == k3:
        self.report({'INFO'}, "Gracias por usar Nodes Elinv!")
        return klrfOIXAc(self)
    elif f1 != f2 or f2 != f3 or f1 != f3 or k1 != k2 or k2 != k3 or k1 != k3:
        self.report({'INFO'}, "Datos incoherentes de registro! Trial ha finalizado!")      
        return [0,0,0,0]
    else:
        print(arch1)
        print(arch2)
        print(arch3)
        print("hola elinv")
        CkpJBFXxf(arch1, idTbCeBGqVI)
        CkpJBFXxf(arch2, idTbCeBGqVI)
        CkpJBFXxf(arch3, idTbCeBGqVI)
        return klrfOIXAc(self)
class CnzXPaTMV(bpy.types.Operator):
    bl_idname = "trial.full"
    bl_label = "Trial to Full"
    def execute(self, context):
        scene = context.scene
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        try:
            s.connect(("www.google.com", 80))
        except (socket.gaierror, socket.timeout):
            scene.keyActivation = "Sin conexión a internet."
        else:
            self.report({'INFO'}, "Registrando...")
            s.close()
            yiirdFDlL(self)
            global k1
            global k2
            global k3
            global f1
            global f2
            global f3        
            if k1 == k2 and k2 == k3 and  k1 == k3: 
                URL = 'https://elinv.musica.ar/nod/'
                inpUN = scene.inpUserName
                inpPW = scene.inpPassword
                key = lzHcXaWfj(k1)
                user = lzHcXaWfj(inpUN)
                password = lzHcXaWfj(inpPW)
                userdata = {"key": key, "user": user, "password": password}
                resp = requests.post(URL, params=userdata)
                resp = resp.text.replace('"', "").replace("[", "").replace("]", "")
                respuesta = resp.split(",")                
                if platform.system() == "Windows":
                    k1 = k1.replace("-", "")
                if respuesta[2]==k1:
                    scene.keyActivation = respuesta[5]
                    uuidKey = gkcd(k1)
                    reg = scene.keyActivation
                    if uuidKey == reg:
                        msg = BtheMweEE(mensajes[2])
                        self.report({'INFO'}, msg)
                        arch4 = BtheMweEE(archivos[3])
                        CkpJBFXxf(arch4, reg)
        return {"FINISHED"}
def WOPiYrfBj(self, context, f, s, c, retorno = False):
    if GfiAtGfzT(self, context) == 1:
        res = yiirdFDlL(self)
        print(res)
        if res[1] == 0:
            self.report({'INFO'}, "Versión Trial finalizada")
            return {"FINISHED"}
        else:
            self.report({'INFO'}, "Trial: " + str(res[2]) + " días de uso!")
            if retorno == True:
                return 0
            elif retorno == False:
                f(s,c)
    elif GfiAtGfzT(self, context) == -1:
        self.report({'INFO'}, "Versión full activada!")
        if retorno == True:
            return 0
        elif retorno == False:
            f(s,c)
    return {"FINISHED"}        
