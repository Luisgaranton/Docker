from flask import request, jsonify
from .app import app
import mercadopago

sdk = mercadopago.SDK("TEST-2082401690503661-010313-094f9ca10138869a7dce6ad3be0a0469-1620054987")


@app.route('/create_order', methods=['POST'])
def create_order():
    try:

        preference_data = {
            "items": [
                {
                    "title": "labial",
                    "quantity": 1,
                    "unit_price": 75.76,
                }
            ]
        }

        preference_response = sdk.preference().create(preference_data)
        preference = preference_response["response"]
        print("Preferencia creada:", preference)

        if preference is None:
            raise ValueError("La preferencia no puede ser nula")
        else:
            # Obtener el URL de Mercado Pago
            mercado_pago_url = preference.get("init_point", None)

        if mercado_pago_url is None:
            raise ValueError("No se encontró 'init_point' en la preferencia")

        return jsonify({"mercado_pago_url": mercado_pago_url})
    except Exception as e:
        print("Error:", str(e))
        return jsonify({'status': 'error'})

