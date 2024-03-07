clienteUno={
    "id":5,
    "nombre":"edef1",
    "consumo":200

}
clienteDos={
    "id":58,
    "nombre":"Edif2",
    "consumo":500

}
clientesAsociados=[
    clienteUno,
    clienteDos
]
for i in range(2):
    print(clientesAsociados[i]["consumo"])

    #programemos un foreach que es un for 
    #especializados en arreglos (lista)
for  cliente in clientesAsociados:
    print(cliente["consumo"])
    print (cliente["id"], "=>", cliente["consumo"],"KWH")
    print(f"{cliente}")
