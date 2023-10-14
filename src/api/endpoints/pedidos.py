from fastapi import APIRouter, HTTPException, HTTPException
from src.db.mysql_connection import create_mysql

router = APIRouter()

@router.get("/")
def pedidosAll():
    try:

        connection = create_mysql()
        cursor = connection.cursor(dictionary=True)
        cursor_sql = """SELECT
            F.fac_fecha AS fac_fecha,
            F.fac_numero_boleta AS numero_boleta,
            C.cli_nombre AS cli_nombre,
            C.cli_celular AS cli_celular,
            C.cli_direccion AS cli_direccion,
            P.pro_nombre AS productos,
            DF.det_cantidad AS pro_cantidad,
            P.pro_precio AS precio_x_unidad,
            (DF.det_cantidad * P.pro_precio) AS pro_precio,
            F.fac_fecha_entrega AS fac_fecha_entrega,
            F.fac_descripcion AS fac_descripcion,
            F.fac_total AS fac_total
        FROM Factura F
        JOIN Cliente C ON F.cliente_id = C.cli_id
        JOIN Detalle_Fac DF ON F.fac_id = DF.factura_id
        JOIN Producto P ON DF.producto_id = P.pro_id;"""
        

        cursor.execute(cursor_sql)
        pedidosAll = cursor.fetchall()
        cursor.close()
        connection.close()
        print("******************DATA ENVIADA***********************")
        print(pedidosAll)
        print("*****************************************************")

        if pedidosAll is None:
            raise HTTPException(status_code = 404, detail="Usuario no encontrado")
        return pedidosAll
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error del servidor: {str(e)}")