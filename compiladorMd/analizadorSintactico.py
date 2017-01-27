# !/usr/bin/env python
# -*- coding: utf-8 -*-
import ply.yacc as yacc
from analizadorLexico import tokens

########################################################################
# documento

def p_documento_lineas(p):
	'documento							: lineas'
	p[0] = '{}'.format(p[1])
	


########################################################################
# lineas

def p_lineas_lineas(p):
	'lineas								: lineas linea'
	p[0] = '{}{}'.format(p[1],p[2])

def p_lineas_linea(p):
	'lineas								: linea'
	p[0] = '{}'.format(p[1])



########################################################################
# elementos1`	q`2

def p_linea_elementos_enters(p):
	'linea								: elementos enters'
	p[0] = '{}{}'.format(p[1],p[2])

def p_linea_elementos(p):
	'linea								: elementos'
	p[0] = '{}'.format(p[1])



########################################################################
# elementos

def p_elementos_elementos(p):
	'elementos							: elementos elemento'
	p[0] = '{}{}'.format(p[1], p[2])

def p_elementos_elemento(p):
	'elementos							: elemento'
	p[0] = '{}'.format(p[1])



########################################################################
# elemento

def p_elemento_separador(p):
	'elemento							: separador'
	p[0] = '{}'.format(p[1])
	
def p_elemento_cita(p):
	'elemento							: cita'
	p[0] = '{}'.format(p[1])

def p_elemento_fecha(p):
	'elemento							: autor'
	p[0] = '{}'.format(p[1])

def p_elemento_fecha(p):
	'elemento							: fecha'
	p[0] = '{}'.format(p[1])

def p_elemento_ulist(p):
	'elemento							: ulist'
	p[0] = '{}'.format(p[1])	

def p_elemento_nlist(p):
	'elemento							: nlist'
	p[0] = '{}'.format(p[1])

def p_elemento_imagen(p):
	'elemento							: imagen'
	p[0] = '{}'.format(p[1])

def p_elemento_enlace(p):
	'elemento							: enlace'
	p[0] = '{}'.format(p[1])

def p_elemento_titulo(p):
	'elemento							: titulo'
	p[0] = '{}'.format(p[1])

def p_elemento_parrafos(p):
	'elemento							: parrafos'
	p[0] = '{}'.format(p[1])

def p_elemento_ecuacion(p):
	'elemento							: fecuacion'
	p[0] = '{}'.format(p[1])

def p_elemento_ccodigos(p):
	'elemento							: ccodigos'
	p[0] = '{}'.format(p[1])



########################################################################
# palabras

def p_palabras_aacen(p):
	'palabras							: AACEN'
	p[0] = '{}'.format(p[1])

def p_palabras_eacen(p):
	'palabras							: EACEN'
	p[0] = '{}'.format(p[1])

def p_palabras_iacen(p):
	'palabras							: IACEN'
	p[0] = '{}'.format(p[1])

def p_palabras_oacen(p):
	'palabras							: OACEN'
	p[0] = '{}'.format(p[1])	

def p_palabras_uacen(p):
	'palabras							: UACEN'
	p[0] = '{}'.format(p[1])

def p_palabras_nacen(p):
	'palabras							: NACEN'
	p[0] = '{}'.format(p[1])

def p_palabras_palabra(p):
	'palabras							: PALABRA'
	p[0] = '{}'.format(p[1])
	


########################################################################
# espacios

def p_espacios_espacios(p):
	'espacios							: espacios ESPACIO'
	p[0] = '{}{}'.format(p[1],p[2])

def p_espacios(p):
	'espacios							: ESPACIO'
	p[0] = ' '.format(p[1])



########################################################################
# enters

def p_enters(p):
	'enters								: enters ENTER'
	p[0] = '\n\t\t<br>\n\t\t<br>'
	
def p_enter(p):
	'enters								: ENTER'
	p[0] = '\n\t\t<br>'



########################################################################
# salto

def p_saltos(p):
	'saltos								: saltos ENTER'
	p[0] = '\t\t<br>'
	
def p_saltos(p):
	'saltos								: ENTER'
	p[0] = '\t\t<br>'.format(p[1])



########################################################################
# titulo

def p_titulo_h1(p):
	'titulo								:	H1 stextos H1'
	p[0] = '\t\t<h1>{}</h1>'.format(p[2])

def p_titulo_h1_atributos(p):
	'titulo								:	H1 stextos H1 IPAREN PALABRA DPAREN'
	p[0] = '\t\t<h1 align="{}">{}</h1>'.format(p[5],p[2])

def p_titulo_h2(p):
	'titulo								:	H2 stextos H2'
	p[0] = '\t\t<h2>{}</h2>'.format(p[2])

def p_titulo_h3(p):
	'titulo								:	H3 stextos H3'
	p[0] = '\t\t<h3>{}</h3>'.format(p[2])

def p_titulo_h4(p):
	'titulo								:	H4 stextos H4'
	p[0] = '\t\t<h4>{}</h4>'.format(p[2])

def p_titulo_h5(p):
	'titulo								:	H5 stextos H5'
	p[0] = '\t\t<h5>{}</h5>'.format(p[2])

def p_titulo_h6(p):
	'titulo								:	H6 stextos H6'
	p[0] = '\t\t<h6>{}</h6>'.format(p[2])



########################################################################
# fecuacion

def p_fecuacion_sin(p):
	'fecuacion							: DOLLARSIGN ecuaciones DOLLARSIGN'
	p[0] = '\t\t\t\n${}$'.format(p[2])

def p_fecuacion(p):
	'fecuacion							: DOLLARSIGN DOLLARSIGN ecuaciones DOLLARSIGN DOLLARSIGN'
	p[0] = '\t\t\t\n$${}$$'.format(p[3])



#~ ########################################################################
#~ # ecuaciones
#~ 
def p_ecuationes_ecuaciones(p):
	'ecuaciones							: ecuaciones ecuacion'
	p[0] = '{}{}'.format(p[1],p[2])

def p_ecuaciones(p):
	'ecuaciones							: ecuacion'
	p[0] = '{}'.format(p[1])



########################################################################
# ecuacion

def p_ecuacion_espacios(p):
	'ecuacion							: espacios'
	p[0] = '{}'.format(p[1])
	
def p_ecuacion_enters(p):
	'ecuacion							: enters'
	p[0] = '{}'.format(p[1])
	
def p_ecuacion_palabras(p):
	'ecuacion							: palabras'
	p[0] = '{}'.format(p[1])

def p_ecuacion_ex(p):
	'ecuacion							: EX'
	p[0] = '{}'.format(p[1])

def p_ecuacion_minus(p):
	'ecuacion							: MEN'
	p[0] = '{}'.format(p[1])

def p_ecuacion_lin(p):
	'ecuacion							: LIN'
	p[0] = '{}'.format(p[1])

def p_ecuacion_per(p):
	'ecuacion							: PER'
	p[0] = '{}'.format(p[1])

def p_ecuacion_plus(p):
	'ecuacion							: PLUS'
	p[0] = '{}'.format(p[1])	

def p_ecuacion_igual(p):
	'ecuacion							: IGUAL'
	p[0] = '{}'.format(p[1])

def p_ecuacion_coma(p):
	'ecuacion							: COMA'
	p[0] = '{}'.format(p[1])
	
def p_ecuacion_colon(p):
	'ecuacion							: COLON'
	p[0] = '{}'.format(p[1])

def p_ecuacion_slash(p):
	'ecuacion							: SLASH'
	p[0] = '{}'.format(p[1])

def p_ecuacion_punto(p):
	'ecuacion							: PUNTO'
	p[0] = '{}'.format(p[1])

def p_ecuacion_amper(p):
	'ecuacion							: AMPER'
	p[0] = '{}'.format(p[1])

def p_ecuacion_under(p):
	'ecuacion							: UNDER'
	p[0] = '{}'.format(p[1])

def p_ecuacion_bslash(p):
	'ecuacion							: BSLASH'
	p[0] = '{}'.format(p[1])
	
def p_ecuacion_bbslash(p):
	'ecuacion							: BBSLASH'
	p[0] = '{}'.format(p[1])
	
def p_ecuacion_lpar(p):
	'ecuacion							: IPAREN'
	p[0] = '{}'.format(p[1])

def p_ecuacion_rpar(p):
	'ecuacion							: DPAREN'
	p[0] = '{}'.format(p[1])

def p_ecuacion_lcur(p):
	'ecuacion							: ILLAVE'
	p[0] = '{}'.format(p[1])

def p_ecuacion_rcur(p):
	'ecuacion							: DLLAVE'
	p[0] = '{}'.format(p[1])
	
def p_ecuacion_numero(p):
	'ecuacion							: NUMERO'
	p[0] = '{}'.format(p[1])

def p_ecuacion_lbra(p):
	'ecuacion							: ICORCHETE'
	p[0] = '{}'.format(p[1])

def p_ecuacion_rbra(p):
	'ecuacion							: DCORCHETE'
	p[0] = '{}'.format(p[1])

def p_ecuacion_semico(p):
	'ecuacion							: SEMICOLON'
	p[0] = '{}'.format(p[1])	

def p_ecuacion_circu(p):
	'ecuacion							: CIRCUMFLEX'
	p[0] = '{}'.format(p[1])

def p_ecuacion_ap(p):
	'ecuacion							: APOSTROPHE'
	p[0] = '{}'.format(p[1])

def p_ecuacion_asteristico(p):
	'ecuacion							: ASTERISCO'
	p[0] = '{}'.format(p[1])


########################################################################
# fecha

def p_fecha(p):
	'fecha								: IGUAL FECHA'
	p[0] = '\t\t<center><script type="text/JavaScript"  style="fecha"> \t\tvar f = new Date(); ' 
	p[0] += '\n\t\t\tdocument.write(f.getDate() + "/" + (f.getMonth() +1) + "/" + f.getFullYear());' 
	p[0] += '\n\t\t</script></center>\n'
	
def p_fecha_fecha(p):
	'fecha								: IGUAL FECHA ILLAVE stextos DLLAVE '
	p[0] = '\n\t\t\t<center><fecha>{}\t\t\t</fecha></center>'.format(p[4])


########################################################################
# separador

def p_separador(p):
	'separador							: DMIN enters'
	p[0] = '\n\t\t<hr>'

def p_separador_espacios(p):
	'separador							: DMIN espacios enters'
	p[0] = '\n\t\t<hr>'
	
def p_separador_atributos_numero(p):
	'separador							: DMIN IPAREN NUMERO DPAREN enters'
	p[0] = '\n\t\t<hr width="{}" align="center">'.format(p[3])
	#~ html.write('<hr width="90%" align="center">')

def p_separador_atributos(p):
	'separador							: DMIN IPAREN NUMERO COMA PALABRA DPAREN enters'
	p[0] = '\n\t\t<hr width="{}" align="{}">'.format(p[3],p[5])
	#~ html.write('<hr width="90%" align="center">')

#~ def p_linea_atributos_c(p):
	#~ 'linea								: DMIN IPAREN PALABRA COMMA NUMERO COMMA PALABRA DPAREN'
	#~ p[0] = '\n\t\t\t<hr color="{}" width="{}" align="{}">\n\t\t\t'.format(p[3],p[5],p[7])
	#~ html.write('<hr width="90%" align="center">')



########################################################################
# autor

def p_autor_autor(p):
	'autor								: IGUAL AUTOR ILLAVE stextos DLLAVE '
	p[0] = '\n\t\t\t<autor>{}\t\t\t</autor>'.format(p[4])



########################################################################
# negrita

def p_negrita(p):
	'negrita							: BO stextos BO'
	p[0] = '<strong>{}</strong>'.format(p[2])



########################################################################
# cnegrita

def p_cnegrita(p):
	'cnegrita							: BOIT stextos BOIT'
	p[0] = '<strong><em>{}</em></strong>'.format(p[2])



########################################################################
# cursiva

def p_cursiva(p):
	'cursiva							: ASTERISCO stextos ASTERISCO'
	p[0] = '<em>{}</em>'.format(p[2])



########################################################################
# subrayado

def p_subrayado(p):
	'subrayado							: UNDER stextos UNDER'
	p[0] = '<u>{}</u>'.format(p[2])


########################################################################
# stextos

def p_stextos(p):
	'stextos							: stextos stexto'
	p[0] = '{}{}'.format(p[1],p[2])

def p_stextos_stext(p):
	'stextos							: stexto'
	p[0] = '{}'.format(p[1])



########################################################################
# stexto

def p_stexto_spaces(p):
	'stexto								: espacios'
	p[0] = '{}'.format(p[1])

def p_stexto_enters(p):
	'stexto								: ENTER'
	p[0] = '<br>'.format(p[1])
	
def p_stexto_palabras(p):
	'stexto								: palabras'
	p[0] = '{}'.format(p[1])
		
def p_stexto_ex(p):
	'stexto								: EX'
	p[0] = '{}'.format(p[1])

def p_stexto_min(p):
	'stexto								: MEN'
	p[0] = '{}'.format(p[1])
	
def p_stext_ast(p):
	'stexto								: AST'
	p[0] = '*'.format(p[1])

def p_stext_menorque(p):
	'stexto								: MENORQUE'
	p[0] = '{}'.format(p[1])

def p_stext_mayorque(p):
	'stexto								: EMAYORQUE'
	p[0] = '>'.format(p[1])
	
def p_stext_gato(p):
	'stexto								: GATO'
	p[0] = '#'.format(p[1])
	
def p_stext_dollar(p):
	'stexto								: DOLLAR'
	p[0] = '$'.format(p[1])
	
#~ def p_stext_per(p):
	#~ 'stexto								: PER'
	#~ p[0] = '{}'.format(p[1])
	
def p_stext_plus(p):
	'stexto								: PLUS'
	p[0] = '{}'.format(p[1])
	
def p_stext_mark(p):
	'stexto								: MARK'
	p[0] = '{}'.format(p[1])
	
def p_stext_imark(p):
	'stexto								: IMARK'
	p[0] = '{}'.format(p[1])

def p_stexto_slash(p):
	'stexto								: SLASH'
	p[0] = '{}'.format(p[1])

def p_stexto_dslash(p):
	'stexto								: DSLASH'
	p[0] = '{}'.format(p[1])

def p_stexto_bslash(p):
	'stexto								: BSLASH'
	p[0] = '{}'.format(p[1])

def p_stexto_amper(p):
	'stexto								: AMPER'
	p[0] = '{}'.format(p[1])

def p_stexto_igual(p):
	'stexto								: IGUAL'
	p[0] = '{}'.format(p[1])
	
def p_stexto_colon(p):
	'stexto								: COLON'
	p[0] = '{}'.format(p[1])
	
def p_stexto_comma(p):
	'stexto								: COMA'
	p[0] = '{}'.format(p[1])
	
def p_stexto_under(p):
	'stexto								: EGUIONBAJO'
	p[0] = '{}'.format(p[1])
	
def p_stexto_punto(p):
	'stexto								: PUNTO'
	p[0] = '{}'.format(p[1])

def p_stexto_lcur(p):
	'stexto								: ILLAVE'
	p[0] = '{}'.format(p[1])

def p_stexto_rcur(p):
	'stexto								: DLLAVE'
	p[0] = '{}'.format(p[1])

def p_stexto_numbero(p):
	'stexto								: NUMERO'
	p[0] = '{}'.format(p[1]) 

def p_stexto_rpar(p):
	'stexto								: IPAREN'
	p[0] = '{}'.format(p[1])

def p_stexto_lpar(p):
	'stexto								: DPAREN'
	p[0] = '{}'.format(p[1])
	
def p_stexto_comillas(p):
	'stexto								: COMILLA'
	p[0] = '{}'.format(p[1])

def p_stexto_lbra(p):
	'stexto								: ICORCHETE'
	p[0] = '{}'.format(p[1])

def p_stexto_rbra(p):
	'stexto								: DCORCHETE'
	p[0] = '{}'.format(p[1])
	
def p_stexto_semi(p):
	'stexto								: SEMICOLON'
	p[0] = '{}'.format(p[1])	

def p_stexto_circu(p):
	'stexto								: CIRCUMFLEX'
	p[0] = '{}'.format(p[1])
	
def p_stexto_apost(p):
	'stexto								: APOSTROPHE'
	p[0] = '{}'.format(p[1])


	
########################################################################
# locacions

def p_locacions_locacions(p):
	'locaciones							: locaciones locacion'
	p[0] = '{}{}'.format(p[1],p[2])
	

def p_locacions(p):
	'locaciones							: locacion'
	p[0] = '{}'.format(p[1])
	


########################################################################
# locacion

def p_locacion_palabras(p):
	'locacion							: palabras'
	p[0] = '{}'.format(p[1])

def p_locacion_jpg(p):
	'locacion							: JPG'
	p[0] = '{}'.format(p[1])

def p_locacion_png(p):
	'locacion							: PNG'
	p[0] = '{}'.format(p[1])

def p_locacion_men(p):
	'locacion							: MEN'
	p[0] = '{}'.format(p[1])	
	
def p_locacion_slash(p):
	'locacion							: SLASH'
	p[0] = '{}'.format(p[1])

def p_locacion_punto(p):
	'locacion							: PUNTO'
	p[0] = '{}'.format(p[1])



########################################################################
# url

def p_url(p):
	'url								: HTTP COLON DSLASH dirs'
	p[0] = '{}{}{}{}'.format(p[1],p[2],p[3],p[4])
	
def p_url_https(p):
	'url								: HTTPS COLON DSLASH dirs'
	p[0] = '{}{}{}{}'.format(p[1],p[2],p[3],p[4])



########################################################################
# dirs

def p_dirs(p):
	'dirs								: dirs dir'
	p[0] = '{}{}'.format(p[1],p[2])
	
def p_dir(p):
	'dirs								: dir'
	p[0] = '{}'.format(p[1])


########################################################################
# dir
def p_dir_palabras(p):
	'dir								: palabras'
	p[0] = '{}'.format(p[1])

def p_dir_h1(p):
	'dir								: H1'
	p[0] = '{}'.format(p[1])

def p_dir_por(p):
	'dir								: PER'
	p[0] = '{}'.format(p[1])

def p_dir_www(p):
	'dir								: WWW'
	p[0] = '{}'.format(p[1])
	
def p_dir_men(p):
	'dir								: MEN'
	p[0] = '{}'.format(p[1])
	
def p_dir_plus(p):
	'dir								: PLUS'
	p[0] = '{}'.format(p[1])

def p_dir_mark(p):
	'dir								: MARK'
	p[0] = '{}'.format(p[1])

def p_dir_igual(p):
	'dir								: IGUAL'
	p[0] = '{}'.format(p[1])

def p_dir_amper(p):
	'dir								: AMPER'
	p[0] = '{}'.format(p[1])

def p_dir_slash(p):
	'dir								: SLASH'
	p[0] = '{}'.format(p[1])
	
def p_dir_under(p):
	'dir								: UNDER'
	p[0] = '{}'.format(p[1])
	
def p_dir_punto(p):
	'dir								: PUNTO'
	p[0] = '{}'.format(p[1])


########################################################################
# cita

def p_cita(p):
	'cita								: MAYORQUE ESPACIO selementos'
	p[0] = '\n\t\t\t<blockquote>{}\n\t\t\t</blockquote>'.format(p[3])




########################################################################
# enlace

def p_enlace(p):
	'enlace								: ICORCHETE stextos DCORCHETE IPAREN url DPAREN'
	p[0] = '<a href="{}">{}</a>'.format(p[5],p[2])




########################################################################
# imagen

def p_imagen(p):
	'imagen								: EX ICORCHETE stextos DCORCHETE IPAREN locaciones DPAREN'
	p[0] = '\t\t\t<div class="imgizq" align="center"s>\n\t\t\t<img src="{}">\n\t\t\t<p>{}</p>\n\t\t</div>\n'.format(p[6],p[3])

def p_imagen_size(p):
	'imagen								: EX ICORCHETE stextos DCORCHETE IPAREN locaciones DPAREN IPAREN NUMERO COMA NUMERO DPAREN'
	p[0] = '\t\t<div class="imgizq" align="center"s>\n\t\t\t<img src="{}" height="{}" width="{}">\n\t\t\t<p>{}</p>\n\t\t</div>\n'.format(p[6],p[11],p[9],p[3])
	
	
	
########################################################################
# ccodigos

def p_ccodigos(p):
	'ccodigos							: COLON COLON COLON codigos COLON COLON COLON'
	p[0] = '\t\t<div class="highlight"><pre>{}</pre></div>'.format(p[4])



########################################################################
# codigos

def p_codigos_codigos(p):
	'codigos							: codigos codigo'
	p[0] = '{}{}'.format(p[1],p[2])

def p_codigos(p):
	'codigos							: codigo'
	p[0] = '{}'.format(p[1])



########################################################################
# codigo

def p_codigo_espa(p):
	'codigo								: espacios'
	p[0] = '{}'.format(p[1])

def p_codigo_tab(p):
	'codigo								: TAB'
	p[0] = '<dd>'

def p_codigo_enters(p):
	'codigo								: saltos'
	p[0] = '{}'.format(p[1])

def p_codigo_palabras(p):
	'codigo								: palabras'
	p[0] = '<span class="s">{}</span>'.format(p[1])
		
def p_codigo_under(p):
	'codigo								: UNDER'
	p[0] = '<span class="s">{}</span>'.format(p[1])

def p_codigo_print(p):
	'codigo								: PRINT'
	p[0] = '<span class="k">print</span>'
	
def p_codigo_printf(p):
	'codigo								: PRINTF'
	p[0] = '<span class="k">printf</span>'

def p_codigo_return(p):
	'codigo								: RETURN'
	p[0] = '<span class="k">return</span>'
	
def p_codigo_if(p):
	'codigo								: IF'
	p[0] = '<span class="k">if</span>'

def p_codigo_else(p):
	'codigo								: ELSE'
	p[0] = '<span class="k">else</span>'

def p_codigo_for(p):
	'codigo								: FOR'
	p[0] = '<span class="k">for</span>'

def p_codigo_class(p):
	'codigo								: CLASS'
	p[0] = '<span class="k">class</span>'

def p_codigo_import(p):
	'codigo								: IMPORT'
	p[0] = '<span class="k">import</span>'
	
def p_codigo_throws(p):
	'codigo								: THROWS'
	p[0] = '<span class="k">throws</span>'
	
def p_codigo_println(p):
	'codigo								: PRINTLN'
	p[0] = '<span class="k">println</span>'
	
def p_codigo_from(p):
	'codigo								: FROM'
	p[0] = '<span class="k">from</span>'

def p_codigo_int(p):
	'codigo								: INT'
	p[0] = '<span class="k">int</span>'

def p_codigo_enum(p):
	'codigo								: ENUM'
	p[0] = '<span class="k">enum</span>'

def p_codigo_void(p):
	'codigo								: VOID'
	p[0] = '<span class="k">void</span>'
	
def p_codigo_public(p):
	'codigo								: PUBLIC'
	p[0] = '<span class="k">public</span>'

def p_codigo_extends(p):
	'codigo								: EXTENDS'
	p[0] = '<span class="k">extends</span>'

def p_codigo_long(p):
	'codigo								: LONG'
	p[0] = '<span class="k">long</span>'

def p_codigo_while(p):
	'codigo								: WHILE'
	p[0] = '<span class="k">while</span>'
	
def p_codigo_switch(p):
	'codigo								: SWITCH'
	p[0] = '<span class="k">switch</span>'
	
def p_codigo_def(p):
	'codigo								: DEF'
	p[0] = '<span class="k">def</span>'
	
def p_codigo_case(p):
	'codigo								: CASE'
	p[0] = '<span class="k">while</span>'
	
def p_codigo_typedef(p):
	'codigo								: TYPEDEF'
	p[0] = '<span class="k">typedef</span>'
	
def p_codigo_getWriter(p):
	'codigo								: GETWRITER'
	p[0] = '<span class="k">getWriterBSLASH</span>'
	
def p_codigo_char(p):
	'codigo								: CHAR'
	p[0] = '<span class="k">char</span>'
	
def p_codigo_continue(p):
	'codigo								: CONTINUE'
	p[0] = '<span class="k">continue</span>'

def p_codigo_do(p):
	'codigo								: DO'
	p[0] = '<span class="k">continue</span>'

def p_codigo_sizeof(p):
	'codigo								: SIZEOF'
	p[0] = '<span class="k">sizeof</span>'

def p_codigo_lib(p):
	'codigo								: MENORQUE palabras MAYORQUE'
	p[0] = '<span class="k">{}{}{}</span>'.format(p[1],p[2],p[3])

def p_codigo_include(p):
	'codigo								: H1 INCLUDE'
	p[0] = '<span class="u">{}{}</span>'.format(p[1],p[2])

def p_codigo_colon(p):
	'codigo								: COLON'
	p[0] = '<span class="u">{}</span>'.format(p[1])

def p_codigo_iparen(p):
	'codigo								: IPAREN'
	p[0] = '<span class="u">{}</span>'.format(p[1])

def p_codigo_dparen(p):
	'codigo								: DPAREN'
	p[0] = '<span class="u">{}</span>'.format(p[1])
	
def p_codigo_illave(p):
	'codigo								: ILLAVE'
	p[0] = '<span class="u">{}</span>'.format(p[1])

def p_codigo_dllave(p):
	'codigo								: DLLAVE'
	p[0] = '<span class="u">{}</span>'.format(p[1])
	
	
def p_codigo_icorchete(p):
	'codigo								: ICORCHETE'
	p[0] = '<span class="u">{}</span>'.format(p[1])

def p_codigo_dcorchete(p):
	'codigo								: DCORCHETE'
	p[0] = '<span class="u">{}</span>'.format(p[1])

def p_codigo_igual(p):
	'codigo								: IGUAL'
	p[0] = '<span class="u">{}</span>'.format(p[1])
	
def p_codigo_coma(p):
	'codigo								: COMA'
	p[0] = '<span class="u">{}</span>'.format(p[1])

def p_codigo_punto(p):
	'codigo								: PUNTO'
	p[0] = '<span class="u">{}</span>'.format(p[1])

def p_codigo_mark(p):
	'codigo								: MARK'
	p[0] = '<span class="u">{}</span>'.format(p[1])

def p_codigo_semicolon(p):
	'codigo								: SEMICOLON'
	p[0] = '<span class="u">{}</span>'.format(p[1])

def p_codigo_mark(p):
	'codigo								: MARK'
	p[0] = '<span class="u">{}</span>'.format(p[1])

def p_codigo_asterisco(p):
	'codigo								: ASTERISCO'
	p[0] = '<span class="u">{}</span>'.format(p[1])
	
def p_codigo_plus(p):
	'codigo								: PLUS'
	p[0] = '<span class="u">{}</span>'.format(p[1])
	
def p_codigo_men(p):	
	'codigo								: MEN'
	p[0] = '<span class="u">{}</span>'.format(p[1])
	
def p_codigo_greather(p):
	'codigo								: MAYORQUE'
	p[0] = '<span class="u">{}</span>'.format(p[1])

def p_codigo_per(p):	
	'codigo								: PER'
	p[0] = '<span class="u">{}</span>'.format(p[1])
	
	
def p_codigo_titi(p):
	'codigo								: APOSTROPHE palabras APOSTROPHE'
	p[0] = '<span class="t">{}{}{}</span>'.format(p[1],p[2],p[3])

def p_codigo_s(p):
	'codigo								: APOSTROPHE stextos APOSTROPHE'
	p[0] = '<span class="t">{}{}{}</span>'.format(p[1],p[2],p[3])

def p_codigo_comilla(p):
	'codigo								: COMILLA stextos COMILLA'
	p[0] = '<span class="t">{}{}{}</span>'.format(p[1],p[2],p[3])
	

def p_codigo_numero(p):
	'codigo								: NUMERO'
	p[0] = '<span class="t">{}</span>'.format(p[1])



########################################################################
# parrafos

def p_parrafos_parrafos(p):
	'parrafos							: parrafos parrafo'
	p[0] = '{}{}'.format(p[1],p[2])

def p_parrafos_parrafo(p):
	'parrafos							: parrafo'
	p[0] = '{}'.format(p[1])



########################################################################
# parrafo

def p_parrafo_autor(p):
	'parrafo							: autor'
	p[0] = ' {} '.format(p[1])

def p_parrafo_espacios(p):
	'parrafo							: espacios'
	p[0] = ' {} '.format(p[1])

def p_parrafo_stextos(p):
	'parrafo							: stextos'
	p[0] = ' {} '.format(p[1])
	
def p_parrafo_enlace(p):
	'parrafo							: enlace'
	p[0] = ' {} '.format(p[1])
	
def p_paragraph_negrita(p):
	'parrafo							: negrita'
	p[0] = ' {} '.format(p[1])

def p_parrafo_cursiva(p):
	'parrafo							: cursiva'
	p[0] = ' {} '.format(p[1])
		
def p_parrafo_cnegrita(p):
	'parrafo							: cnegrita'
	p[0] = ' {} '.format(p[1])
	
def p_parrafo_subrayado(p):
	'parrafo							: subrayado'
	p[0] = ' {} '.format(p[1])
	
def p_parrafo_fecuaction(p):
	'parrafo							: fecuacion'
	p[0] = ' {} '.format(p[1])



########################################################################
# ulist

def p_ulist(p):
	'ulist								: uitems'
	p[0] = '<ul>\n{}\n</ul>'.format(p[1])



########################################################################
# uitems

def p_uitems_uitems(p):
	'uitems								: uitems uitem'
	p[0] = '{}\n{}'.format(p[1], p[2])
	
def p_uitems_uitem(p):
	'uitems								: uitem'
	p[0] = '{}'.format(p[1])



########################################################################
# uitem

def p_uitem_space(p):
	'uitem								: ASTERISCO ESPACIO palabras ENTER'
	p[0] = '<li>{}</li>'.format(p[3])

def p_uitem(p):
	'uitem								: ASTERISCO palabras ENTER'
	p[0] = '<li>{}</li>'.format(p[2])
	
	
	
########################################################################
# nlist

def p_nlist(p):
	'nlist								: nitems'
	p[0] = '\n\t\t<ol>\n{}\n\t\t</ol>'.format(p[1])



########################################################################
# nitems

def p_nitems_nitems(p):
	'nitems								: nitems nitem'
	p[0] = '{}\n{}'.format(p[1], p[2])
	
def p_nitems_nitem(p):
	'nitems								: nitem'
	p[0] = '{}'.format(p[1])



########################################################################
# nitem

def p_nitem_space(p):
	'nitem								: NUMERO PUNTO ESPACIO palabras ENTER'
	p[0] = '\t\t\t<li>{}</li>'.format(p[4])

def p_nitem(p):
	'nitem								: NUMERO PUNTO palabras ENTER'
	p[0] = '\t\t\t<li>{}</li>'.format(p[3])






########################################################################
# selementos 

def p_selementos_selementos(p):
	'selementos							: selementos selemento'
	p[0] = '{}{}'.format(p[1],p[2])

def p_selementos(p):
	'selementos							: selemento'
	p[0] = '{}'.format(p[1])



########################################################################
# selementos 

def p_selemento_negritas(p):
	'selemento							: negrita'
	p[0] = '\t\t\t{}'.format(p[1])

def p_selemento_citas(p):
	'selemento							: cita'
	p[0] = '\t\t\t{}'.format(p[1])
	
def p_selemento_stextos(p):
	'selemento							: stextos'
	p[0] = '\t\t\t{}'.format(p[1])

def p_selementos_cursiva(p):
	'selemento							: cursiva'
	p[0] = '\t\t\t{}'.format(p[1])



########################################################################
# error

def p_error(p):
	print("Syntax error: {}".format(p))



########################################################################
# parser

def parser():
	return yacc.yacc()

