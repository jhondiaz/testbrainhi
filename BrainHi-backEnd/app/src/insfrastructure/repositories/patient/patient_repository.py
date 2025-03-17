import requests
from src.core.domain.entities.patient import Patient
from src.core.domain.interfaces.repositorys.patient_repository import IPatientRepository
from src.core.domain.shemas.response_repository import RepoResponse





class PatientRepository(IPatientRepository):
   
    async def save(self, patient: Patient)->RepoResponse:
      try:  
 
            patient_data = {
                "resourceType": "Patient",
                "name":[{"use": name.use, "family": name.family, "given": name.given} for name in patient.name],
                "gender": patient.gender,
                "birthDate": patient.birthDate
            }

            headers = {
                    "Content-Type": "application/json"
                }
            # Convertir a JSON y enviar al servidor FHIR
            response = requests.post(f"http://hapi.fhir.org/baseR4/Patient", json=patient_data,headers=headers)
            print(response)
            if response.status_code in [200, 201]:  # Creación exitosa
              return RepoResponse(IsSuccess=True, Value=response.json(), Message ="Paciente registrado en FHIR")
            else:
              return RepoResponse(IsSuccess=True, Value=response.json(), Message ="No se pudo registrar el paciente")   
          

      
      except requests.exceptions.RequestException as e:
            return RepoResponse(IsSuccess=False, Value={str(e)}, Message =f"No se pudo conectar al servidor FHIR: {str(e)}")   
         
      except Exception as e:
            return RepoResponse(IsSuccess=False, Value={str(e)}, Message =f"Error inesperado: {str(e)}")   
          
        
    async def getById(self, id :str)->RepoResponse:
      try:  
       
            headers = {
                    "Content-Type": "application/json"
                }
            # Convertir a JSON y enviar al servidor FHIR
            response = requests.get(f"http://hapi.fhir.org/baseR4/Patient/{id}", headers=headers)
            print(response)
            if response.status_code in [200, 201]:  # Creación exitosa
              return RepoResponse(IsSuccess=True, Value=response.json(), Message ="Paciente consultado en FHIR")
            else:
              return RepoResponse(IsSuccess=True, Value=response.json(), Message ="No se pudo consultar el paciente")   
          

      
      except requests.exceptions.RequestException as e:
            return RepoResponse(IsSuccess=False, Value={str(e)}, Message =f"No se pudo conectar al servidor FHIR: {str(e)}")   
         
      except Exception as e:
            return RepoResponse(IsSuccess=False, Value={str(e)}, Message =f"Error inesperado: {str(e)}")   
          
        

  

  