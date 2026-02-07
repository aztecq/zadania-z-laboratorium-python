# Ćwiczenie 12: Cykl Życia Projektu
import requests

response = requests.get("https://httpbin.org/get")
print("Status:", response.status_code)
print("Połączono pomyślnie!")