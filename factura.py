import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


print("         DONAS COLOMBIA S.A           ")
print("NIT: 860508791-1")
print("RESPONSABLE DE IVA. CI IU 1081")
print("Agente Retenedor de ICA")
print("        TELEFONO : 2100200")
print("servicioalclientedonascolombia.com.co")
print("         AVENIDA MAX DUQUE")
print("         DG 23 69 55 LC 126")
print("Aut. DIAN 18764027319797  FEC 01/04/2022")
print("Vigencia Hasta:31/03/2023")

actual =datetime.datetime.now()

hora =datetime.datetime.now().hour
min =datetime.datetime.now().minute
seg =datetime.datetime.now().second

print("FECHA: {}/{}/{}".format(actual.day,actual.month,actual.year))
print("HORA: {}:{}:{}".format(actual.hour,actual.minute,actual.second))

print("--ESTA SIENDO ATENDIDO POR:-")
print("cajera:LAURA PRIETO")
class Cliente:
  def __init__(self):
    self.nom=""
    self.telefono=""
    self.cedula=""
  


  def solicitar_datos(self):
    print("-----------------------------")
    print("----DATOS DEL CLIENTE-------- ")
    print("-------------------------------")
    self.nom= input("Escribe tu nombre:")
    self.telefono =input("Escribe tu telefono:")
    self.cedula=input("Escribe tu cedula:")

  def productos (self):
    print("-----------------------------")
    print("-----------PRODUCTO----------")
    print("-----------------------------")
    self.nombre= input("Escribe nombre del producto:")
    self.precio = int(input("Escribe el precio:"))
    self.cantidad= int(input("Escribe la cantidad del producto:"))
  
    self.total=self.precio * self.cantidad 
    self.iva=self.total*0.19
    self.iva_total=(self.total+self.iva)

  def mostrar_resultados(self):
      print("TOTAL:",self.total)
      print("IVA:",self.iva)
      print("TOTAL + IVA:",self.iva_total)
      print("---------------------------------")
      print("-------METODO DE PAGO------------")
      print("----------EFECTIVO---------------")
      print("---------------------------------")
      print("------GRACIAS POR TU COMPRA------")
      print("---------------------------------")



  def mostrar_pdf (self):
    w, h =letter
    c = canvas.Canvas("factura.pdf", pagesize=letter)
    c.setLineWidth(.2)
    c.setFont("Helvetica",10)
    c.drawString(250, h - 30, "DONAS COLOMBIA S.A ")
    c.drawString(251, h - 42, "NIT: 860508791-1 ")
    c.drawString(198, h - 55, "RESPONSABLE DE IVA: CI IU 1081 ")
    c.drawString(238, h - 67, "Agente Retenedor de ICA")
    c.drawString(236, h -79, "TELEFONO : 2100200")
    c.drawString(210,h -90, "servicioalclientedonascolombia.com.co")
    c.drawString(248,h -101, "   AVENIDA MAX DUQUE")
    c.drawString(248,h -113, "   DG 23 69 55 LC 126")
    c.drawString(175,h-140,"Aut. DIAN 18764027319797  FEC 01/04/2022")
    c.drawString(175,h-152,"DESDE JK-33449  HASTA JK-100000")
    c.drawString(175,h-164,f"FECHA: {datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year}     HORA:{hora}:{min}:{seg}")
    c.drawString(175,h-176,"ESTAS SIENDO ATENTIDO POR:")
    c.drawString(175,h -188, "CAJERA:LAURA PRIETO")
    c.drawString(175,h-200,"=================================================")
    c.drawString(175,h-210,"               DATOS DEL  CLIENTE                   ")
    c.drawString(175,h-224,f"NOMBRE: {self.nom}")
    c.drawString(175,h-236,f"TELEFONO: {self.telefono}")
    c.drawString(175,h-248,f"CEDULA: {self.cedula}")
    c.drawString(175,h-272,"=================================================")
    c.drawString(175,h-284,"Uds      DESCRIPCION              PRECIO           TOTAL")
    c.drawString(175,h-296,f"{self.cantidad}             {self.nombre}                                {self.precio}     {self.iva_total}                                                 ")
    c.drawString(175,h-308,"=================================================")
    c.drawString(175,h-320,f"                                                    subtotal:{self.total} ")
    c.drawString(175,h-332,"                                                     DTO 0%           0     ")
    c.drawString(175,h-344,f"                                                     TOTAL:{self.iva_total}  " )
    c.drawString(175,h-356,"=================================================")
    c.drawString(175,h-368,"            DISCRIMINACION DE IMPUESTOS                  " )
    c.drawString(175,h-380,f"     I BASE 19%                                 {self.total}                ")
    c.drawString(175,h-392,f"     TOTAL:                                          {self.iva_total}       ")
    c.drawString(175,h-404,"=================================================")
    c.drawString(175,h-416,"                METODO DE PAGO                   ")
    c.drawString(175,h-428,f"            EFECTIVO                                  {self.iva_total}      ")
    c.drawString(175,h-443,"==================================================")
    c.drawString(175,h-458,"         !!!!!!!!!!!!GRACIAS POR TU COMPRA!!!!!!                                     ")
    c.drawString(175,h-468,"                 unete a nuestro programa de                                               ")
    c.drawString(175,h-480,"           FIDELIZACION CON DONAS COLOMBIA S.A!!                                         ")
    c.drawImage("Donascolombia.png",250,h-580, width=100, height=100)
    c.drawString(175,h-587,"               https://donascolo.000webhostapp.com/                           ")
    c.drawString(175,h-600,"                 REGISTRATE CON EL CODIGO:77                                    ")
    c.drawString(175,h-612,"=================================================")
    c.drawString(175,h-620,"     TIQUETE POS IMPRESO Por software lpfrontrest                                    ")
    c.drawString(175,h-632,"        DESARROLLADO POR LPE NIT: 282883838                                 ")
    c.drawString(175,h-648,"=================================================")
    c.drawString(175,h-657,"      SI REQUIERE FACTURA ELECTRONICA DE VENTA                                   ")
    c.drawString(175,h-669,"  SOLICITELA ABJUTANDO SU RUT Y FOTO DE ESTE TIQUETE                                ")
    c.drawString(175,h-680,"       servicioalcliente@donascolombia.com                                            ")
    c.save()

fac=Cliente()
fac.solicitar_datos()
fac.productos()
fac.mostrar_resultados()
fac.mostrar_pdf()
