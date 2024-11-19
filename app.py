from flask import Flask, jsonify

app = Flask(__name__)

# Datos de ejemplo
animales = {
    "vertebrados": [
        {"nombre": "Gato", "tipo": "Mamífero", "caracteristicas": "Pelo, 4 patas"},
        {"nombre": "Perro", "tipo": "Mamífero", "caracteristicas": "Pelo, 4 patas"},
        {"nombre": "Loro", "tipo": "Ave", "caracteristicas": "Plumas, 2 patas"},
        {"nombre": "Salmón", "tipo": "Pez", "caracteristicas": "Aletas, branquias"},
        {"nombre": "Rana", "tipo": "Anfibio", "caracteristicas": "Piel húmeda, 4 patas"},
        {"nombre": "Tortuga", "tipo": "Reptil", "caracteristicas": "Caparazón, 4 patas"},
        {"nombre": "Ballena", "tipo": "Mamífero", "caracteristicas": "Acuático, 2 aletas"},
        {"nombre": "Cocodrilo", "tipo": "Reptil", "caracteristicas": "Piel escamosa, 4 patas"},
        {"nombre": "Aguila", "tipo": "Ave", "caracteristicas": "Plumas, 2 patas"},
        {"nombre": "Serpiente", "tipo": "Reptil", "caracteristicas": "Sin patas"},
        {"nombre": "Tiburón", "tipo": "Pez", "caracteristicas": "Aletas, branquias"},
        {"nombre": "Río", "tipo": "Anfibio", "caracteristicas": "Piel húmeda, 4 patas"},
        {"nombre": "Gallo", "tipo": "Ave", "caracteristicas": "Plumas, 2 patas"},
        {"nombre": "Elefante", "tipo": "Mamífero", "caracteristicas": "Grande, trompa"},
        {"nombre": "Cebra", "tipo": "Mamífero", "caracteristicas": "Rayas, 4 patas"},
    ],
    "invertebrados": [
        {"nombre": "Abeja", "tipo": "Insecto", "caracteristicas": "Alas, 6 patas"},
        {"nombre": "Mariposa", "tipo": "Insecto", "caracteristicas": "Alas, 6 patas"},
        {"nombre": "Araña", "tipo": "Arácnido", "caracteristicas": "8 patas"},
        {"nombre": "Medusa", "tipo": "Cnidario", "caracteristicas": "Cuerpo gelatinoso"},
        {"nombre": "Caracol", "tipo": "Gasterópodo", "caracteristicas": "Concha, 1 pie"},
        {"nombre": "Estrella de mar", "tipo": "Equinodermo", "caracteristicas": "5 brazos"},
        {"nombre": "Pulpo", "tipo": "Mollusco", "caracteristicas": "8 brazos"},
        {"nombre": "Cangrejo", "tipo": "Crustáceo", "caracteristicas": "10 patas"},
        {"nombre": "Lombriz", "tipo": "Anélido", "caracteristicas": "Cuerpo segmentado"},
        {"nombre": "Mosca", "tipo": "Insecto", "caracteristicas": "Alas, 6 patas"},
        {"nombre": "Termita", "tipo": "Insecto", "caracteristicas": "Alas, 6 patas"},
        {"nombre": "Gusano", "tipo": "Anélido", "caracteristicas": "Cuerpo alargado"},
        {"nombre": "Coral", "tipo": "Cnidario", "caracteristicas": "Colonias de pólipos"},
        {"nombre": "Anémona", "tipo": "Cnidario", "caracteristicas": "Tentáculos"},
        {"nombre": "Camarón", "tipo": "Crustáceo", "caracteristicas": "10 patas"},
    ]
}

@app.route('/api/animales', methods=['GET'])
def get_animales():
    return jsonify(animales)

if __name__ == '__main__':
    app.run(debug=True)