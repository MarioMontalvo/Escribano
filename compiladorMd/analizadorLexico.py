# !/usr/bin/env python
# -*- coding: utf-8 -*-
import ply.lex as lex

# Palabras reservadas
reserved = {
	'include'		: 'INCLUDE',
	'getWriter'		: 'GETWRITER',
	'throws'		: 'THROWS',
	'println' 		: 'PRINTLN',
	'void'			: 'VOID',
	'extends'		: 'EXTENDS',
	'public'		: 'PUBLIC',
	'return'		: 'RETURN',
	'from'			: 'FROM',
	'sizeof'		: 'SIZEOF',
	'do'			: 'DO',
	'char'			: 'CHAR',
	'continue'		: 'CONTINUE',
	'typedef'		: 'TYPEDEF',
	'switch'		: 'SWITCH',
	'case'  		: 'CASE',
	'int'   		: 'INT',
	'enum'  		: 'ENUM',
	'float' 		: 'FLOAT',
	'long ' 		: 'LONG',
	'from'  		: 'FROM',
	'print' 		: 'PRINT',
	'printf' 		: 'PRINTF',
	'if' 			: 'IF',
	'else' 			: 'ELSE',
	'for' 			: 'FOR',
	'while' 		: 'WHILE',
	'def' 			: 'DEF',
	'class' 		: 'CLASS',
	'import'		: 'IMPORT',
	'www'   		: 'WWW',
	'png'   		: 'PNG',
	'jpg'   		: 'JPG',
	'http'  		: 'HTTP',
	'fecha' 		: 'FECHA',
	'autor' 		: 'AUTOR',
	'https' 		: 'HTTPS',
}
# Lista de tokens
tokens = [
	'ENTER',
	'ESPACIO',
# ********************************* Titulos *******************************
	'H1',
	'H2',
	'H3',
	'H4',
	'H5',
	'H6',
# ********************************* Enfasis *******************************
	'BO',
	'TAB',
	'BOIT',
	'ASTERISCO',
	'AACEN',
	'EACEN',
	'IACEN',
	'OACEN',
	'UACEN',
	'NACEN',
	'NUMERO',
	'PALABRA',
# ******************************* Parentesis ******************************
	'IPAREN',
	'DPAREN',
	'ILLAVE',
	'DLLAVE',
	'ICORCHETE',
	'DCORCHETE',
# ********************************* Signos ********************************
	'AST',
	'GATO',
	'DOLLAR',
	'EMAYORQUE',
	'EGUIONBAJO',
# ********************************* Signos ********************************
	'EX',
	'PER',
	'MEN',
	'DMIN',
	'LIN',
	'PLUS',
	'MARK',
	'IMARK',
	'IGUAL',
	'PUNTO',
	'UNDER',
	'AMPER',
	'SLASH',
	'COLON',
	'COMA',
	'BSLASH',
	'BBSLASH',
	'DSLASH',
	'MAYORQUE',
	'MENORQUE',
	'COMILLA',
	'SEMICOLON',
	'DOLLARSIGN',
	'CIRCUMFLEX',
	'APOSTROPHE',
]
tokens += reserved.values()

# Expresiones regulares para tokens
# ******************************* Cracteres para escapar *********************************
t_TAB       = r'\t'
t_AST       = r'\\\*'
t_GATO      = r'\\\#'
t_DOLLAR    = r'\\\$'
t_EMAYORQUE = r'\\\>'
t_EGUIONBAJO = r'\\\>_'
# ******************************* Titulos *********************************
t_H1 = '\#'
t_H2 = '\#\#'
t_H3 = '\#\#\#'
t_H4 = '\#\#\#\#'
t_H5 = '\#\#\#\#\#'
t_H6 = '\#\#\#\#\#\#'
t_ENTER      = r'\n'
t_ESPACIO    = r'\ '
t_DOLLARSIGN = '\$'
# ******************************* Enfasis *********************************
t_BO         = r'\*\*'
t_BOIT    	 = r'\*\*\*'
t_ASTERISCO  = r'\*'
# ***************************** Parentesis ********************************
t_ILLAVE    = r'\{'
t_DLLAVE    = r'\}'
t_IPAREN    = r'\('
t_DPAREN    = r'\)'
t_ICORCHETE = r'\['
t_DCORCHETE = r'\]'

# ******************************* Signos **********************************
t_EX    = r'\!'
t_PER   = r'%'
t_MEN   = r'-'
t_LIN   = r'\|'
t_DMIN  = r'\-\-'
t_PLUS  = r'\+'
t_MARK  = r'\?'
t_IMARK = r'\¿'
t_UNDER = r'_'
t_AMPER = r'\&'
t_PUNTO = r'\.'

t_COLON = r':'
t_COMA = r','
t_IGUAL = r'='

t_SLASH = r'/'
t_BSLASH = r'\\'
t_BBSLASH = r'\\\\'
t_DSLASH = r'//'

t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_SEMICOLON = ';'
t_CIRCUMFLEX = r'\^'
t_APOSTROPHE = '\''
t_COMILLA = '\"'

t_AACEN = r'á'
t_EACEN = r'é'
t_IACEN = r'í'
t_OACEN = r'ó'
t_UACEN = r'ú'
t_NACEN = r'ñ'


t_NUMERO = r'[0-9]+'

def t_PALABRA(t):
	r'[a-zA-Z]+'
	if t.value in reserved:
		t.type = reserved[ t.value ]
	return t


def t_error(t):
	 print("Illegal character '%s'" % t.value[0])
	 t.lexer.skip(1)

lex = lex.lex()
