# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtWebKit
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtWebKit import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from compiadorMd import *
from externos import *

VERSION = '0.1'
ESTILO = 'css/black.css'

class VentanaPrincipal(QtGui.QWidget):

	def __init__(self):
		super(VentanaPrincipal, self).__init__()
		self.filen = ''
		self.initUI()


	def initUI(self):
		####################################################  QTextEdit #####################################################

		self.editor = QtGui.QTextEdit(self)
		self.editor.move(8, 50)
		self.editor.resize(650,690)
		self.editor.setStyleSheet("background-color: #ffffff; border-radius: 10px; border: 3px solid #808080")
		QtCore.QObject.connect(self.editor, QtCore.SIGNAL('textChanged()'), self.onTextChanged)
		self.editor.changesSaved = True


		####################################################  QWebView ######################################################

		self.visorWeb = QtWebKit.QWebView(self)
		self.visorWeb.move(665,50)
		self.visorWeb.resize(650,690)
		self.visorWeb.load(QtCore.QUrl('htmlArchivos/frontV2.html'))
		self.visorWeb.setStyleSheet("background-color: #ffffff; border-radius: 80px; border: 10px solid #909090")


		####################################################  QMenuBar ######################################################

		self.menu = QtGui.QMenuBar(self)
		archivoMenu = self.menu.addMenu('Archivo')
		herramietasMenu = self.menu.addMenu('Herramientas')
		ayudaMenu = self.menu.addMenu('Ayuda')


		nuevoArchivo = QtGui.QAction(QtGui.QIcon("iconos/nuevo.png"),"Nuevo",self)
		nuevoArchivo.setShortcut('Ctrl+N')
		nuevoArchivo.setStatusTip('Nuevo')
		nuevoArchivo.triggered.connect(self.nuevoArchivoF)

		abrirArchivo = QtGui.QAction(QtGui.QIcon("iconos/abrir.png"),"Abrir",self)
		abrirArchivo.setShortcut('Ctrl+O')
		abrirArchivo.setStatusTip('Abrir')
		abrirArchivo.triggered.connect(self.abrirArchivo)

		guardarArchivo = QtGui.QAction(QtGui.QIcon("iconos/guardar.png"),"Guardar",self)
		guardarArchivo.setShortcut('Ctrl+S')
		guardarArchivo.setStatusTip('Guardar')
		guardarArchivo.triggered.connect(self.guardarArchivo)

		exportarPDF = QtGui.QAction(QtGui.QIcon("iconos/pdf.png"),'Exportar PDF',self)
		exportarPDF.triggered.connect(self.exportarPDF)

		salir = QtGui.QAction(QtGui.QIcon('iconos/salir.png'),'Salir', self)
		salir.setShortcut('Ctrl+Q')
		salir.triggered.connect(self.closeEvent)


		orientacion = QtGui.QAction('Orientacion ', self)
		orientacion.triggered.connect(self.paintEvent)

		ayuda = QtGui.QAction(QtGui.QIcon("iconos/ayuda.png"), 'Ayuda', self)
		ayuda.setShortcut('F1')
		ayuda.setStatusTip('Ayuda ')
		ayuda.triggered.connect(self.ayudaFuncion)

		acerca = QtGui.QAction(QtGui.QIcon("iconos/acerca.png"),'Acerca de...', self)
		acerca.triggered.connect(self.acercaFuncion)

		temas = herramietasMenu.addMenu(QtGui.QIcon('iconos/estilos.png'),'Estilos')
		estilo0 = QtGui.QAction(QtGui.QIcon('iconos/estilos.png'),'Estilo negro', self)
		estilo0.setShortcut('Ctrl+X')
		estilo0.setStatusTip('Estilo negro')
		estilo0.triggered.connect(self.estilo0Funcion)
		temas.addAction(estilo0)

		estilo1 = QtGui.QAction(QtGui.QIcon('iconos/estilos.png'),'Estilo gray', self)
		estilo1.setShortcut('Ctrl+X')
		estilo1.setStatusTip('Buscar')
		estilo1.triggered.connect(self.estilo1Funcion)
		temas.addAction(estilo1)

		estilo2 = QtGui.QAction(QtGui.QIcon('iconos/estilos.png'),'Estilo azul', self)
		estilo2.setShortcut('Ctrl+X')
		estilo2.setStatusTip('Estilo azul')
		estilo2.triggered.connect(self.estilo2Funcion)
		temas.addAction(estilo2)

		estilo3 = QtGui.QAction(QtGui.QIcon('iconos/estilos.png'),'Theme green', self)
		estilo3.setShortcut('Ctrl+X')
		estilo3.setStatusTip('Estilo azul')
		estilo3.triggered.connect(self.estilo3Funcion)
		temas.addAction(estilo3)

		archivoMenu.addAction(nuevoArchivo)
		archivoMenu.addAction(abrirArchivo)
		archivoMenu.addAction(guardarArchivo)
		archivoMenu.addAction(exportarPDF)
		archivoMenu.addAction(salir)
		ayudaMenu.addAction(ayuda)
		ayudaMenu.addAction(acerca)



		####################################################  QPushButtons ##################################################

		###############################  Buton Nuevo #####################################

		self.botonNuevo = QtGui.QPushButton('', self)
		self.botonNuevo.setIcon(QtGui.QIcon(QtGui.QPixmap('iconos/nuevo.png')))
		self.botonNuevo.setIconSize(QtCore.QSize(25,25))
		self.botonNuevo.clicked.connect(self.nuevoArchivoF)
		self.botonNuevo.move(5, 10)
		self.botonNuevo.setStyleSheet("border-radius: 10px; border-width:0px")



		###############################  Button Abrir #####################################

		self.botonAbrir = QtGui.QPushButton('', self)
		self.botonAbrir.setIcon(QtGui.QIcon(QtGui.QPixmap('iconos/abrir.png')))
		self.botonAbrir.setIconSize(QtCore.QSize(25,25))
		self.botonAbrir.clicked.connect(self.abrirArchivo)
		self.botonAbrir.move(36, 10)
		self.botonAbrir.setStyleSheet("border-radius: 10px; border-width:0px")



		###############################  Buton Guardar #####################################

		self.botonGuardar = QtGui.QPushButton('', self)
		self.botonGuardar.setIcon(QtGui.QIcon(QtGui.QPixmap('iconos/guardar.png')))
		self.botonGuardar.setIconSize(QtCore.QSize(23,23))
		self.botonGuardar.clicked.connect(self.guardar)
		self.botonGuardar.move(67, 10)
		self.botonGuardar.setStyleSheet("border-radius: 10px; border-width:0px")



		###############################  Button imagen ###################################

		self.botonImagen = QtGui.QPushButton('', self)
		self.botonImagen.setIcon(QtGui.QIcon(QtGui.QPixmap('iconos/imagen.png')))
		self.botonImagen.setIconSize(QtCore.QSize(22,22))
		self.botonImagen.clicked.connect(self.insertarImagen)
		self.botonImagen.move(210, 10)
		self.botonImagen.setStyleSheet("border-radius: 10px; border-width:0px")



		###############################  Button Ecuacion #################################

		self.botonEcuacion = QtGui.QPushButton('', self)
		self.botonEcuacion.setIcon(QtGui.QIcon(QtGui.QPixmap('iconos/ecuacion.png')))
		self.botonEcuacion.setIconSize(QtCore.QSize(22,22))
		self.botonEcuacion.clicked.connect(self.ecuacion)
		self.botonEcuacion.move(240, 10)
		self.botonEcuacion.setStyleSheet("border-radius: 10px; border-width:0px")



		###############################  Button Lista ####################################

		self.botonLista = QtGui.QPushButton('', self)
		self.botonLista.setIcon(QtGui.QIcon(QtGui.QPixmap('iconos/lista.png')))
		self.botonLista.setIconSize(QtCore.QSize(23,23))
		self.botonLista.clicked.connect(self.lista)
		self.botonLista.move(275, 10)
		self.botonLista.setStyleSheet("border-radius: 10px; border-width:0px")



		###############################  Button Lista no numerada ########################

		self.botonListaN = QtGui.QPushButton('', self)
		self.botonListaN.setIcon(QtGui.QIcon(QtGui.QPixmap('iconos/listaN.png')))
		self.botonListaN.setIconSize(QtCore.QSize(23,23))
		self.botonListaN.clicked.connect(self.listaN)
		self.botonListaN.move(310, 10)
		self.botonListaN.setStyleSheet("border-radius: 10px; border-width:0px")



		###############################  Button Buscar ##################################

		self.botonBuscar = QtGui.QPushButton('', self)
		self.botonBuscar.setIcon(QtGui.QIcon(QtGui.QPixmap('iconos/buscar.png')))
		self.botonBuscar.setIconSize(QtCore.QSize(23,23))
		self.botonBuscar.clicked.connect(find.Find(self).show)
		self.botonBuscar.move(440, 10)
		self.botonBuscar.setStyleSheet('border-radius: 10px; border-width:0px')

		self.botonBuscar = QtGui.QPushButton('', self)
		self.botonBuscar.setIcon(QtGui.QIcon(QtGui.QPixmap('casosdeuso.jpg')))
		self.botonBuscar.setIconSize(QtCore.QSize(23,23))
		self.botonBuscar.clicked.connect(find.Find(self).show)
		self.botonBuscar.move(440, 10)
		self.botonBuscar.setStyleSheet('border-radius: 10px; border-width:0px')

		###############################  Button Preview ##################################

		self.buttonPreview  = QtGui.QPushButton('', self)
		self.buttonPreview.setIcon(QtGui.QIcon(QtGui.QPixmap('iconos/preview.png')))
		self.buttonPreview.setIconSize(QtCore.QSize(23,23))
		self.buttonPreview.clicked.connect(self.preview)
		self.buttonPreview.move(470, 10)
		self.buttonPreview.setStyleSheet("border-radius: 10px; border-width:0px")


		###############################  Button Copiar #####################################

		self.botonCopiar  = QtGui.QPushButton('', self)
		self.botonCopiar.setIcon(QtGui.QIcon(QtGui.QPixmap('iconos/copiar.png')))
		self.botonCopiar.setIconSize(QtCore.QSize(23,23))
		self.botonCopiar.clicked.connect(self.editor.copy)
		self.botonCopiar.move(500, 10)
		self.botonCopiar.setStyleSheet("border-radius: 10px; border-width:0px")



		###############################  Buttonar Pegar ####################################

		self.botonPegar  = QtGui.QPushButton('', self)
		self.botonPegar.setIcon(QtGui.QIcon(QtGui.QPixmap('iconos/pegar.png')))
		self.botonPegar.setIconSize(QtCore.QSize(23,23))
		self.botonPegar.clicked.connect(self.editor.paste)
		self.botonPegar.move(530, 10)
		self.botonPegar.setStyleSheet("border-radius: 10px; border-width:0px")



		###############################  Button Deshacer #####################################

		self.botonDeshacer = QtGui.QPushButton('', self)
		self.botonDeshacer.setIcon(QtGui.QIcon(QtGui.QPixmap('iconos/deshacer.png')))
		self.botonDeshacer.setIconSize(QtCore.QSize(20,20))
		self.botonDeshacer.clicked.connect(self.editor.undo)
		self.botonDeshacer.move(560, 10)
		self.botonDeshacer.setStyleSheet("border-radius: 10px; border-width:0px")



		###############################  Button Hacer #####################################

		self.botonHacer = QtGui.QPushButton('', self)
		self.botonHacer.setIcon(QtGui.QIcon(QtGui.QPixmap('iconos/hacer.png')))
		self.botonHacer.setIconSize(QtCore.QSize(20,20))
		self.botonHacer.clicked.connect(self.editor.redo)
		self.botonHacer.move(590, 10)
		self.botonHacer.setStyleSheet("border-radius: 10px; border-width:0px")



		###############################  Button Cortar  ##################################

		self.butonCortar  = QtGui.QPushButton('', self)
		self.butonCortar.setIcon(QtGui.QIcon(QtGui.QPixmap('iconos/cortar.png')))
		self.butonCortar.setIconSize(QtCore.QSize(23,23))
		self.butonCortar.clicked.connect(self.editor.cut)
		self.butonCortar.move(620, 10)
		self.butonCortar.setStyleSheet("border-radius: 10px; border-width:0px")


		##########################  Button Configuracion #################################

		#~ self.buttonConf  = QtGui.QPushButton('', self)
		#~ self.buttonConf.setIcon(QtGui.QIcon(QtGui.QPixmap('iconos/confiV2.png')))
		#~ self.buttonConf.setIconSize(QtCore.QSize(27,27))
		#~ self.buttonConf.move(665, 10)
		#~ self.buttonConf.setStyleSheet("border-radius: 10px; border-width:0px")


		###############################  Button Ayuda ####################################

		self.butonAyuda  = QtGui.QPushButton('', self)
		self.butonAyuda.setIcon(QtGui.QIcon(QtGui.QPixmap('iconos/ayudaV2.png')))
		self.butonAyuda.setIconSize(QtCore.QSize(30,27))
		self.butonAyuda.clicked.connect(self.ayudaFuncion)
		self.butonAyuda.move(665, 10)
		self.butonAyuda.setStyleSheet("border-radius: 10px; border-width:0px")


		###############################  Button PDF ####################################

		self.buttonPDF  = QtGui.QPushButton('', self)
		self.buttonPDF.setIcon(QtGui.QIcon(QtGui.QPixmap('iconos/pdfV2.png')))
		self.buttonPDF.setIconSize(QtCore.QSize(25,25))
		self.buttonPDF.clicked.connect(self.exportarPDF)
		self.buttonPDF.move(1225, 10)
		self.buttonPDF.setStyleSheet("border-radius: 10px; border-width:0px")



		#############################  Button Recargar ###################################

		self.botonRecargar = QtGui.QPushButton('', self)
		self.botonRecargar.setIcon(QtGui.QIcon(QtGui.QPixmap('iconos/recargarV2.png')))
		self.botonRecargar.setIconSize(QtCore.QSize(25,25))
		self.botonRecargar.clicked.connect(self.onTextChanged)
		self.botonRecargar.move(1255, 10)
		self.botonRecargar.setStyleSheet("border-radius: 10px; border-width:0px")

		############################  Button Salir #######################################

		self.botonSalir = QtGui.QPushButton('', self)
		self.botonSalir.setIcon(QtGui.QIcon(QtGui.QPixmap('iconos/quitv2.png')))
		self.botonSalir.setIconSize(QtCore.QSize(25,25))
		self.botonSalir.clicked.connect(self.cerrarEvento)
		self.botonSalir.move(1285, 10)
		self.botonSalir.setStyleSheet("border-radius: 10px; border-width:0px")


		####################################################   Ventana  ######################################################

		self.setWindowTitle('Escribano%s' % VERSION)
		self.setWindowIcon(QtGui.QIcon('iconos/icon_pen.png'))
		self.setGeometry(0, 0, 1500, 900)
		self.show()


	def font_choice(self):
		font, valid = QtGui.QFontDialog.getFont()
		if valid:
			self.styleChoice.setFont(font)


	def abrirArchivo(self):
		nombre = QtGui.QFileDialog.getOpenFileName(self, 'Abrir archivo', '/home')
		archivo = open(nombre, 'r')
		datos = archivo.read()
		archivo.close()
		self.editor.setText(datos)


	def guardarArchivo(self):
		nombre = QtGui.QFileDialog.getSaveFileName(self, 'Guardar', "", ".conf")
		n =  nombre + '.md'
		archivo = open(n ,'w')
		archivo.write(self.editor.toPlainText())
		archivo.close()


	def guardar(self):
		if not self.filen:
			self.filen = QtGui.QFileDialog.getSaveFileName(self, 'Guardar')
		if self.filen:
			if not str(self.filen).endswith(".md"):
				self.filen += ".md"
			with open(self.filen,"wt") as file:
				file.write(self.textEdit.toHtml())
			self.changesSaved = True


	def nuevoArchivoF(self):
		self.editor.clear()

	def onTextChanged(self):
		#print(self.editor.toPlainText())
		#t = str(self.editor.toPlainText())
		#escribirMd(t)
		#self.visorWeb.load(QtCore.QUrl("html/index.html"))
		obser = unicode(self.editor.toPlainText())
		obser1 = obser.encode('utf-8')
		#print obser1
		escribirMd(obser1)
		self.visorWeb.load(QtCore.QUrl("htmlArchivos/index.html"))


	def exportarPDF(self):
		filename = QtGui.QFileDialog.getSaveFileName(self, "Guardar PDF", "", ".conf")
		printer = QPrinter()
		printer.setPageSize(QPrinter.A4)
		printer.setOutputFormat(QPrinter.PdfFormat)
		printer.setOutputFileName(filename+".pdf")
		self.visorWeb.print_(printer)


	def ayudaFuncion(self):
		self.visorWeb.load(QtCore.QUrl('html/ayuda.html'))


	def acercaFuncion(self):
		aboutWin = aboutWindow().exec_()


	def estilo0Funcion(self):
		global ESTILO
		ESTILO = "css/negro.css"
		self.onTextChanged()


	def estilo1Funcion(self):
		global ESTILO
		ESTILO = "css/gris.css"
		self.onTextChanged()


	def estilo2Funcion(self):
		global ESTILO
		ESTILO = "css/azul.css"
		self.onTextChanged()


	def estilo3Funcion(self):
		global ESTILO
		ESTILO = "css/verde.css"
		self.onTextChanged()

				#~
	#~ def cerrarEvento(self, event):
		#~ reply = QtGui.QMessageBox.question(self, 'Salir Escribano', "Estas seguro de salir de Escribano?",
			#~ QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
		#~ if reply == QtGui.QMessageBox.Yes:
			#~ event.accept()
		#~ else:
			#~ event.ignore()
				#~
	def cerrarEvento(self, event):

		if self.changesSaved:
			event.accept()

		else:
			popup = QtGui.QMessageBox(self)
			popup.setIcon(QtGui.QMessageBox.Warning)
			popup.setText("The document has been modified")
			popup.setInformativeText("Do you want to save your changes?")
			popup.setStandardButtons(QtGui.QMessageBox.Save   | QtGui.QMessageBox.Cancel | QtGui.QMessageBox.Discard)
			popup.setDefaultButton(QtGui.QMessageBox.Save)
			answer = popup.exec_()
			if answer == QtGui.QMessageBox.Save:
				self.save()

			elif answer == QtGui.QMessageBox.Discard:
				event.accept()
			else:
				event.ignore()

	def imprimirPDF(self):
		dialog = QtGui.QPrintDialog()
		if dialog.exec_() == QtGui.QDialog.Accepted:
			self.visorWeb.document().print_(dialog.printer())


	def listaN(self):
		cursor = self.editor.textCursor()
		cursor.insertText('* \n')


	def lista(self):
		cursor = self.editor.textCursor()
		cursor.insertText('1. \n')


	def ecuacion(self):
		cursor = self.editor.textCursor()
		cursor.insertText('$$ m = x + y $$')


	def preview(self):
		preview = QtGui.QPrintPreviewDialog()
		#preview.paintRequested.connect(lambda p: self.textEdit.print_(p))
		preview.exec_()


	def insertarImagen(self):
		imagen = QtGui.QFileDialog.getOpenFileName(self, 'Insert image',".","Images (*.png *.xpm *.jpg *.bmp *.gif)")
		cursor = self.editor.textCursor()
		cursor.insertText('![Titulo de la imagen]({})(400,200)'.format(imagen))


def escribirMd(texto):
	#entrada = open('index.md', 'w')
	#entrada.write(texto)
	#entrada.close()
	escribirhtml(texto)


def escribirhtml(texto):

	html = open('htmlArchivos/index.html','w')
	html.write('<!DOCTYPE HTML>\n')
	html.write('<html>\n')
	html.write('\t<head>\n')
	html.write('\t\t<meta charset="UTF-8">\n')
	html.write('\t\t<link rel="stylesheet" href="/mermaid/mermaid.forest.css"/>\n')
	html.write('\t\t<script src="/mermaid-master/bin/mermaid.js"></script>\n')
	html.write('\t\t<title>Escribano </title>\n')
	html.write('\t\t<link href="{}" rel="stylesheet" type="text/css">\n'.format(ESTILO))
	html.write('\t\t<script type="text/x-mathjax-config">\n')
	html.write('\t\tMathJax.Hub.Config({\n')
	html.write('\t\textensions: ["tex2jax.js"],\n')
	html.write('\t\tjax: ["input/TeX","output/HTML-CSS"],\n')
	html.write('\t\ttex2jax: {inlineMath: [["$","$"],["$$","$$"]]}\n')
	html.write('\t\t});')
	html.write('\n\t\t</script>\n')
	html.write('\t\t<script type="text/javascript" src="MathJax-2.5-latest/MathJax.js"></script>\n')
	html.write('\t</head>\n\n')

	html.write('\t<body style="text-align: justify;">\n')
	parser = analizadorSintactico.parser().parse(texto)
	html.write(parser)
	html.write('\n\t</body>\n\n')
	html.write('</html>\n')
	html.close()


def main():
	print 'Iniciando Escribano ...'
	aplicacion = QtGui.QApplication(sys.argv)
	ventanaPrincipal = VentanaPrincipal()
	sys.exit(aplicacion.exec_())

if __name__ == '__main__':
	main()
