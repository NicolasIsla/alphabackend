import easyocr as ocr  #OCR

from PIL import Image #Image Processing
import numpy as np #Image Processing 

from pysentimiento import create_analyzer

# transformer
from spanlp.palabrota import Palabrota




class model_NLP:
    def __init__(self):
        # pysentimiento
        self.pysentimiento_sentimiento = create_analyzer(task="sentiment", lang="es")
        self.pysentimiento_odio = create_analyzer(task="hate_speech", lang="es")
        self.pysentimiento_emociones = create_analyzer(task="emotion", lang="es")
        self.spanlp_palabrota = Palabrota()
        

        self.texto = None
        
    def preprocesamiento(self, list):
        self.texto  = ' '.join(list)

    def palabrotas(self):
        return self.spanlp_palabrota.contains_palabrota(self.texto)

    def analizar_sentimiento(self):
        # Realizar predicción de sentimiento
        resultado = self.pysentimiento_sentimiento.predict(self.texto)
        return resultado
    
    def analizar_odio(self):
        # Realizar predicción de odio
        resultado = self.pysentimiento_odio.predict(self.texto)
        return resultado
    
    def analizar_emociones(self):
        # Realizar predicción de emociones
        resultado = self.pysentimiento_emociones.predict(self.texto)
        return resultado

    def predict(self, list):
        self.preprocesamiento(list)

        return self.palabrotas(), self.analizar_sentimiento(), self.analizar_odio(), self.analizar_emociones()
    
def analizar_imagen(img_array):
    
    reader = ocr.Reader(['es'],model_storage_directory='.')
    result = reader.readtext(img_array)
    result_text = [] #empty list for results

    for text in result:
        result_text.append(text[1])

    nlp_model = model_NLP()

    caracteristicas_result = []

    palabrotas, sentido, odio, emocion = nlp_model.predict(result_text)
    if palabrotas:
        caracteristicas_result.append(1)
    else:
        caracteristicas_result.append(0)
    
    for model in [sentido, odio, emocion]:
        for key in model.probas.keys():

            caracteristicas_result.append(model.probas[key])

    return caracteristicas_result

    # batch_size = 6
    # for i in range(0, len(result_text)):
    #     try:
    #         batch = result_text[i:i+batch_size]
    #         models = nlp_model.predict(batch)
    #     except:
    #         batch = result_text[i:-1]
    #         models = nlp_model.predict(batch)


    #     for model in models:
    #         vector = []
    #         try:
    #             for key in model.probas.keys():
    #                 vector.append(model.probas[key])
    #         except:
    #             if model:
    #                 vector.append(1)
    #             else:
    #                 vector.append(0)      
    #     caracteristicas_result.append(vector)  
    #   

    # return np.amax(np.array(caracteristicas_result), axis=1)