#Passo 1: Importar as bibliotecas necessárias
from keras.models import Sequential
from keras.layers import Dense

#Passo 2: Definir os dados de entrada e saída
entrada = [[0,0], [0,1], [1,0], [1,1]]
saida = [0, 1, 1, 0]

#Passo 3: Definir o modelo da rede neural
model = Sequential()
model.add(Dense(4, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))


#Passo 4: Compilar o modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#Passo 5: Treinar o modelo
model.fit(entrada, saida, epochs=500, batch_size=4)

#Passo 6: Testar o modelo
resultado = model.predict(entrada)
print(resultado)