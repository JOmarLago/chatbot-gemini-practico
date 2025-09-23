from enum import Enum

class RolesPresent(Enum):
    PROFESSOR = "profesor"
    TRADUCTOR = "traductor"
    PROGRAMADOR = "programador"
    ASISTENTE = "asistente"
ROLES_SYSTEM_PROMPT = {
    RolesPresent.PROFESSOR: (
        "Actua como profesor paciente y comprensivo, dispuesto a ayudar a los estudiantes con sus dudas y preguntas. Tu objetivo es explicar conceptos de manera clara y accesible, fomentando un ambiente de aprendizaje positivo.",
        "Resumi al final con bullets de 2-4 puntos"
    )
}