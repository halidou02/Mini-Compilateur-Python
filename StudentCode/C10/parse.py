import AST
import ply.yacc as yacc
from lex import tokens
import os
import sys
import io


def p_programme(p):                                     #le noued principal de programmes qui contient toutes les fonctions et le main
    '''programme : functions'''
    p[0] = p[1]


def p_functions(p):                                     #les functions + main (le main est obligatoire dans ce grammaire)
    '''functions : function functions
                 | function_main'''
    p[0] = AST.ProgramNode([p[1]])


def p_function(p):                                      #le grammaire d'un function 
    '''function : identifiant LPAREN arguments RPAREN declarations LSEPARATEUR bodyexp RSEPARATEUR
                | type identifiant LPAREN arguments RPAREN declarations LSEPARATEUR bodyexp roteurexp RSEPARATEUR'''
    if len(p) == 10:
        p[0] = AST.FunctionsNode(p[2], p[4], p[6], p[8])
    else:
        p[0] = AST.FunctionsNode(p[1], p[2], p[4], p[6])


def p_function_main(p):                                 #grammaire de main function
    '''function_main : idmain LPAREN RPAREN declarations LSEPARATEUR bodyexp RSEPARATEUR
                     | type idmain LPAREN RPAREN declarations LSEPARATEUR bodyexp roteurexp RSEPARATEUR'''
    if len(p) == 8:
        p[0] = AST.FunctionsNode(p[1], [], p[4], p[6])
    else:
        p[0] = AST.FunctionsNode(p[2], [], p[5], p[7])


def p_identifiant(p):                               
    '''identifiant : ID'''
    p[0] = AST.TokenNode(p[1])


def p_idmain(p):                                        #identifiant de main function 
    '''idmain : MAIN'''
    p[0] = AST.TokenNode(p[1])


def p_functions_type(p):                                #le type de function
    '''type : ENTIER'''
    p[0] = AST.TokenNode(p[1])


def p_arguments(p):                                     #des functions peut contient des arguments  plus le cas d'un function sans grammaire
    '''arguments : argument
                 | EPSILON'''


def p_argument(p):                                      #grammaires des arguments 
    '''argument : ENTIER ID
                | ENTIER ID COMMA argument
                | ENTIER ID LCROCHET RCROCHET
                | ENTIER ID LCROCHET RCROCHET argument
                | number
                | number COMMA argument'''


def p_EPSILON(p):                                       #epsilon represent un vide
    '''EPSILON : '''


def p_declarations(p):                                  #les function et le main peut contients de declaration ou non
    '''declarations : declaration
                    | EPSILON'''


def p_declaration(p):                                  #le grammaire de declaration
    '''declaration : ENTIER list_var ENDLINE
                   | ENTIER ID
                   | ENTIER ID COMMA declaration
                   | ENTIER ID LCROCHET RCROCHET
                   | ENTIER ID LCROCHET RCROCHET declaration'''


def p_list_var(p):                                    #grammaire de cas ou il ya plusieurs variables de meme type
    '''list_var : ID
                | ID COMMA list_var
                | ID LCROCHET RCROCHET
                | ID LCROCHET RCROCHET COMMA list_var'''


def p_bodyexp(p):                                       #grammaire des expressions qui peut etre dans le cœur de fonction
    '''bodyexp : expressions'''
    if len(p) == 2:
        p[0] = AST.BodyNode(p[1])
    else:
        p[0] = []


def p_roteurexp(p):                                     #grammaire d'expression de retour
    '''roteurexp : RETOUR expression_op ENDLINE'''
    p[0] = [AST.ReturnNode(p[2])]


def p_expressions(p):                                       #les expression qui peut etre ecrit dans le main de chaque fonction + si + sinon + affectation + lire + ecrire
    '''expressions : expression expressions
                   | expression_fcall
                   | EPSILON'''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        p[0] = []


def p_expression_affect(p):                                 #grammaire d'affectation
    '''expression : ID AFFECT expression_fcall
                  | ID LCROCHET expression_op RCROCHET AFFECT expression_fcall
                  | ID AFFECT expression_op ENDLINE
                  | ID LCROCHET expression_op RCROCHET AFFECT expression_op ENDLINE'''
    p[0] = AST.AssignNode(p[1], p[3])


def p_expression_si(p):
    '''expression : SI comparison_op ALORS LSEPARATEUR expressions RSEPARATEUR SINON LSEPARATEUR expressions RSEPARATEUR
                  | SI comparison_op ALORS LSEPARATEUR expressions RSEPARATEUR'''
    if len(p) == 11:
        p[0] = AST.SiNode(p[2], p[5], p[9])
    else:
        p[0] = AST.SiNode(p[2], p[5])


def p_expression_tantque(p):
    '''expression : TANTQUE comparison_op FAIRE LSEPARATEUR expressions RSEPARATEUR'''
    p[0] = AST.WhileNode(p[2], p[5])


def p_expression_lire(p):
    '''expression : LIRE LPAREN identifiant RPAREN ENDLINE'''
    p[0] = AST.ReadNode(p[3])


def p_expression_ecrire(p):
    '''expression : ECRIRE LPAREN expression_op RPAREN ENDLINE
                  | ECRIRE LPAREN string_id RPAREN ENDLINE'''
    p[0] = AST.PrintNode(p[3])


def p_string_id(p):                                     
    '''string_id : STRING'''
    p[0] = AST.TokenNode(p[1])


def p_expression_fcall(p):                                                                 #grammaire d'appel d'un function
    '''expression_fcall : ID LPAREN expression_op RPAREN ENDLINE
                       | ID LPAREN string_id RPAREN ENDLINE
                       | ID LPAREN RPAREN ENDLINE'''


def p_expression_op_entier(p):                                                             #les operation arthmitique
    '''expression_op : expression_op ADD_OP expression_op
                     | expression_op MUL_OP expression_op
                     | comparison_op'''
    if len(p) == 4:
        p[0] = AST.OperationNode(p[2], p[1], p[3])
    else:
        p[0] = p[1]


def p_comparison_op(p):                                                                     #les operation de comparison
    '''comparison_op : expression_op LOGC_OP expression_op'''
    p[0] = AST.OperationNode(p[2], p[1], p[3])


def p_comparison_op_par(p):                                                                #comparison peut etre entre parenthese
    '''comparison_op : LPAREN comparison_op RPAREN'''
    p[0] = p[2]


def p_expression_op_var(p):                                                                #les arguments entre parenthese d'un appel function
    '''expression_op : ID COMMA expression_op
                     | number COMMA expression_op'''


def p_expression_op_value(p):                                                           #le rempalcement d'un expression arthemitique
    '''expression_op : ID
                     | number'''
    p[0] = AST.TokenNode(p[1])


def p_expression_op_par(p):                                                             #operation arthemitique peut etre entre parenthese
    '''expression_op : LPAREN expression_op RPAREN'''
    p[0] = p[2]


def p_number(p):                                                                        #le numero et le numero signé
    '''number : ADD_OP NUMBER
              | NUMBER'''
    if len(p) == 3:
        p[0] = AST.OperationNode(p[1], 0, p[2])
    else:
        p[0] = AST.TokenNode(p[1])


def p_error(p):
    print("Not accepted")
    sys.exit(1)


def parse(program):                                                             #partie importé de chatGPT pour eliminer les erreurs des parsers
    output_buffer = io.StringIO()
    sys.stdout = output_buffer
    result = yacc.parse(program)
    sys.stdout = sys.__stdout__
    output = output_buffer.getvalue()
    output_buffer.close()
    return result, output


current_file_path = os.path.abspath(__file__)

current_directory = os.path.dirname(current_file_path)

generated_dir = os.path.join(current_directory, "generated")

yacc.yacc(outputdir=generated_dir)


def read_file(filename):
    with open(filename, 'r') as file:
        f = file.read()
    return f


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: missing file argument")
        sys.exit(1)

    filename = sys.argv[1]
    prog = read_file(filename)
    result = yacc.parse(prog)
    print("Accepted")
