
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD_OP AFFECT ALORS COMMA ECRIRE ENDLINE ENTIER FAIRE ID LCROCHET LIRE LOGC_OP LPAREN LSEPARATEUR MAIN MUL_OP NUMBER RCROCHET RETOUR RPAREN RSEPARATEUR SI SINON STRING TANTQUEprogramme : functionsfunctions : function functions\n                 | function_mainfunction : identifiant LPAREN arguments RPAREN declarations LSEPARATEUR bodyexp RSEPARATEUR\n                | type identifiant LPAREN arguments RPAREN declarations LSEPARATEUR bodyexp roteurexp RSEPARATEURfunction_main : idmain LPAREN RPAREN declarations LSEPARATEUR bodyexp RSEPARATEUR\n                     | type idmain LPAREN RPAREN declarations LSEPARATEUR bodyexp roteurexp RSEPARATEURidentifiant : IDidmain : MAINtype : ENTIERarguments : argument\n                 | EPSILONargument : ENTIER ID\n                | ENTIER ID COMMA argument\n                | ENTIER ID LCROCHET RCROCHET\n                | ENTIER ID LCROCHET RCROCHET argument\n                | number\n                | number COMMA argumentEPSILON : declarations : declaration\n                    | EPSILONdeclaration : ENTIER list_var ENDLINE\n                   | ENTIER ID\n                   | ENTIER ID COMMA declaration\n                   | ENTIER ID LCROCHET RCROCHET\n                   | ENTIER ID LCROCHET RCROCHET declarationlist_var : ID\n                | ID COMMA list_var\n                | ID LCROCHET RCROCHET\n                | ID LCROCHET RCROCHET COMMA list_varbodyexp : expressionsroteurexp : RETOUR expression_op ENDLINEexpressions : expression expressions\n                   | expression_fcall\n                   | EPSILONexpression : ID AFFECT expression_fcall\n                  | ID LCROCHET expression_op RCROCHET AFFECT expression_fcall\n                  | ID AFFECT expression_op ENDLINE\n                  | ID LCROCHET expression_op RCROCHET AFFECT expression_op ENDLINEexpression : SI comparison_op ALORS LSEPARATEUR expressions RSEPARATEUR SINON LSEPARATEUR expressions RSEPARATEUR\n                  | SI comparison_op ALORS LSEPARATEUR expressions RSEPARATEURexpression : TANTQUE comparison_op FAIRE LSEPARATEUR expressions RSEPARATEURexpression : LIRE LPAREN identifiant RPAREN ENDLINEexpression : ECRIRE LPAREN expression_op RPAREN ENDLINE\n                  | ECRIRE LPAREN string_id RPAREN ENDLINEstring_id : STRINGexpression_fcall : ID LPAREN expression_op RPAREN ENDLINE\n                       | ID LPAREN string_id RPAREN ENDLINE\n                       | ID LPAREN RPAREN ENDLINEexpression_op : expression_op ADD_OP expression_op\n                     | expression_op MUL_OP expression_op\n                     | comparison_opcomparison_op : expression_op LOGC_OP expression_opcomparison_op : LPAREN comparison_op RPARENexpression_op : ID COMMA expression_op\n                     | number COMMA expression_opexpression_op : ID\n                     | numberexpression_op : LPAREN expression_op RPARENnumber : ADD_OP NUMBER\n              | NUMBER'
    
_lr_action_items = {'ID':([0,3,6,9,19,35,42,45,49,52,56,57,61,65,69,70,71,74,78,79,84,87,89,91,99,100,101,104,105,110,113,117,121,123,131,137,139,140,141,144,145,146,148,149,150,151,153,155,],[8,8,8,-10,27,44,55,55,55,55,75,75,80,55,88,75,75,75,8,75,-4,75,-36,75,75,75,75,75,75,80,80,-38,-49,55,55,-5,88,-47,-48,-43,-44,-45,-37,-41,-42,-39,55,-40,]),'ENTIER':([0,3,12,23,25,26,28,31,37,40,47,61,83,84,137,],[9,9,19,19,35,35,19,35,19,35,19,35,35,-4,-5,]),'MAIN':([0,3,6,9,84,137,],[10,10,10,-10,-4,-5,]),'$end':([1,2,4,11,67,115,],[0,-1,-3,-2,-6,-7,]),'LPAREN':([5,7,8,10,13,14,55,56,57,58,59,69,70,71,74,79,87,88,91,99,100,101,104,105,139,],[12,15,-8,-9,23,24,71,74,74,78,79,91,91,91,74,91,91,71,91,91,91,91,91,91,91,]),'RPAREN':([8,12,15,16,17,18,20,22,23,24,27,29,30,39,46,47,64,71,75,76,92,94,96,97,102,103,107,108,109,118,124,125,126,127,128,129,130,],[-8,-19,25,26,-11,-12,-17,-61,-19,31,-13,-60,40,-18,-14,-15,-16,95,-57,-58,-52,120,122,-46,127,128,132,133,134,128,-53,-50,-51,-54,-59,-55,-56,]),'ADD_OP':([12,22,23,28,29,37,47,56,57,69,70,71,72,73,74,75,76,77,79,87,88,90,91,92,93,94,99,100,101,102,103,104,105,108,116,118,124,125,126,127,128,129,130,139,147,],[21,-61,21,21,-60,21,21,21,21,21,21,21,-52,100,21,-57,-58,-52,21,21,-57,100,21,-52,100,100,21,21,21,-52,100,21,21,100,100,100,100,100,100,-54,-59,100,100,21,100,]),'NUMBER':([12,21,23,28,37,47,56,57,69,70,71,74,79,87,91,99,100,101,104,105,139,],[22,29,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'COMMA':([20,22,27,29,44,75,76,80,83,88,135,],[28,-61,37,-60,61,104,105,110,113,104,113,]),'LOGC_OP':([22,29,72,73,75,76,77,88,90,92,93,94,102,103,108,116,118,124,125,126,127,128,129,130,147,],[-61,-60,-52,99,-57,-58,-52,-57,99,-52,99,99,-52,99,99,99,99,99,99,99,-54,-59,99,99,99,]),'MUL_OP':([22,29,72,73,75,76,77,88,90,92,93,94,102,103,108,116,118,124,125,126,127,128,129,130,147,],[-61,-60,-52,101,-57,-58,-52,-57,101,-52,101,101,-52,101,101,101,101,101,101,101,-54,-59,101,101,101,]),'ENDLINE':([22,29,43,44,75,76,80,82,83,88,90,92,95,116,120,122,124,125,126,127,128,129,130,132,133,134,135,136,147,],[-61,-60,60,-27,-57,-58,-27,-28,-29,-57,117,-52,121,138,140,141,-53,-50,-51,-54,-59,-55,-56,144,145,146,-29,-30,151,]),'RCROCHET':([22,29,38,62,75,76,92,93,111,124,125,126,127,128,129,130,],[-61,-60,47,83,-57,-58,-52,119,135,-53,-50,-51,-54,-59,-55,-56,]),'ALORS':([22,29,72,75,76,92,124,125,126,127,128,129,130,],[-61,-60,98,-57,-58,-52,-53,-50,-51,-54,-59,-55,-56,]),'FAIRE':([22,29,75,76,77,92,124,125,126,127,128,129,130,],[-61,-60,-57,-58,106,-52,-53,-50,-51,-54,-59,-55,-56,]),'LSEPARATEUR':([25,26,31,32,33,34,36,40,41,44,48,60,81,83,98,106,112,152,],[-19,-19,-19,42,-20,-21,45,-19,49,-23,65,-22,-24,-25,123,131,-26,153,]),'LCROCHET':([27,44,55,80,],[38,62,70,111,]),'SI':([42,45,49,52,65,89,117,121,123,131,140,141,144,145,146,148,149,150,151,153,155,],[56,56,56,56,56,-36,-38,-49,56,56,-47,-48,-43,-44,-45,-37,-41,-42,-39,56,-40,]),'TANTQUE':([42,45,49,52,65,89,117,121,123,131,140,141,144,145,146,148,149,150,151,153,155,],[57,57,57,57,57,-36,-38,-49,57,57,-47,-48,-43,-44,-45,-37,-41,-42,-39,57,-40,]),'LIRE':([42,45,49,52,65,89,117,121,123,131,140,141,144,145,146,148,149,150,151,153,155,],[58,58,58,58,58,-36,-38,-49,58,58,-47,-48,-43,-44,-45,-37,-41,-42,-39,58,-40,]),'ECRIRE':([42,45,49,52,65,89,117,121,123,131,140,141,144,145,146,148,149,150,151,153,155,],[59,59,59,59,59,-36,-38,-49,59,59,-47,-48,-43,-44,-45,-37,-41,-42,-39,59,-40,]),'RSEPARATEUR':([42,45,50,51,52,53,54,63,68,86,89,114,117,121,123,131,138,140,141,142,143,144,145,146,148,149,150,151,153,154,155,],[-19,-19,67,-31,-19,-34,-35,84,-33,115,-36,137,-38,-49,-19,-19,-32,-47,-48,149,150,-43,-44,-45,-37,-41,-42,-39,-19,155,-40,]),'RETOUR':([49,51,52,53,54,65,66,68,85,89,117,121,140,141,144,145,146,148,149,150,151,155,],[-19,-31,-19,-34,-35,-19,87,-33,87,-36,-38,-49,-47,-48,-43,-44,-45,-37,-41,-42,-39,-40,]),'AFFECT':([55,119,],[69,139,]),'STRING':([71,79,],[97,97,]),'SINON':([149,],[152,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programme':([0,],[1,]),'functions':([0,3,],[2,11,]),'function':([0,3,],[3,3,]),'function_main':([0,3,],[4,4,]),'identifiant':([0,3,6,78,],[5,5,13,107,]),'type':([0,3,],[6,6,]),'idmain':([0,3,6,],[7,7,14,]),'arguments':([12,23,],[16,30,]),'argument':([12,23,28,37,47,],[17,17,39,46,64,]),'EPSILON':([12,23,25,26,31,40,42,45,49,52,65,123,131,153,],[18,18,34,34,34,34,54,54,54,54,54,54,54,54,]),'number':([12,23,28,37,47,56,57,69,70,71,74,79,87,91,99,100,101,104,105,139,],[20,20,20,20,20,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,]),'declarations':([25,26,31,40,],[32,36,41,48,]),'declaration':([25,26,31,40,61,83,],[33,33,33,33,81,112,]),'list_var':([35,61,110,113,],[43,82,82,136,]),'bodyexp':([42,45,49,65,],[50,63,66,85,]),'expressions':([42,45,49,52,65,123,131,153,],[51,51,51,68,51,142,143,154,]),'expression':([42,45,49,52,65,123,131,153,],[52,52,52,52,52,52,52,52,]),'expression_fcall':([42,45,49,52,65,69,123,131,139,153,],[53,53,53,53,53,89,53,53,148,53,]),'comparison_op':([56,57,69,70,71,74,79,87,91,99,100,101,104,105,139,],[72,77,92,92,92,102,92,92,102,92,92,92,92,92,92,]),'expression_op':([56,57,69,70,71,74,79,87,91,99,100,101,104,105,139,],[73,73,90,93,94,103,108,116,118,124,125,126,129,130,147,]),'roteurexp':([66,85,],[86,114,]),'string_id':([71,79,],[96,109,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programme","S'",1,None,None,None),
  ('programme -> functions','programme',1,'p_programme','parse.py',10),
  ('functions -> function functions','functions',2,'p_functions','parse.py',15),
  ('functions -> function_main','functions',1,'p_functions','parse.py',16),
  ('function -> identifiant LPAREN arguments RPAREN declarations LSEPARATEUR bodyexp RSEPARATEUR','function',8,'p_function','parse.py',21),
  ('function -> type identifiant LPAREN arguments RPAREN declarations LSEPARATEUR bodyexp roteurexp RSEPARATEUR','function',10,'p_function','parse.py',22),
  ('function_main -> idmain LPAREN RPAREN declarations LSEPARATEUR bodyexp RSEPARATEUR','function_main',7,'p_function_main','parse.py',30),
  ('function_main -> type idmain LPAREN RPAREN declarations LSEPARATEUR bodyexp roteurexp RSEPARATEUR','function_main',9,'p_function_main','parse.py',31),
  ('identifiant -> ID','identifiant',1,'p_identifiant','parse.py',39),
  ('idmain -> MAIN','idmain',1,'p_idmain','parse.py',44),
  ('type -> ENTIER','type',1,'p_functions_type','parse.py',49),
  ('arguments -> argument','arguments',1,'p_arguments','parse.py',54),
  ('arguments -> EPSILON','arguments',1,'p_arguments','parse.py',55),
  ('argument -> ENTIER ID','argument',2,'p_argument','parse.py',59),
  ('argument -> ENTIER ID COMMA argument','argument',4,'p_argument','parse.py',60),
  ('argument -> ENTIER ID LCROCHET RCROCHET','argument',4,'p_argument','parse.py',61),
  ('argument -> ENTIER ID LCROCHET RCROCHET argument','argument',5,'p_argument','parse.py',62),
  ('argument -> number','argument',1,'p_argument','parse.py',63),
  ('argument -> number COMMA argument','argument',3,'p_argument','parse.py',64),
  ('EPSILON -> <empty>','EPSILON',0,'p_EPSILON','parse.py',68),
  ('declarations -> declaration','declarations',1,'p_declarations','parse.py',72),
  ('declarations -> EPSILON','declarations',1,'p_declarations','parse.py',73),
  ('declaration -> ENTIER list_var ENDLINE','declaration',3,'p_declaration','parse.py',77),
  ('declaration -> ENTIER ID','declaration',2,'p_declaration','parse.py',78),
  ('declaration -> ENTIER ID COMMA declaration','declaration',4,'p_declaration','parse.py',79),
  ('declaration -> ENTIER ID LCROCHET RCROCHET','declaration',4,'p_declaration','parse.py',80),
  ('declaration -> ENTIER ID LCROCHET RCROCHET declaration','declaration',5,'p_declaration','parse.py',81),
  ('list_var -> ID','list_var',1,'p_list_var','parse.py',85),
  ('list_var -> ID COMMA list_var','list_var',3,'p_list_var','parse.py',86),
  ('list_var -> ID LCROCHET RCROCHET','list_var',3,'p_list_var','parse.py',87),
  ('list_var -> ID LCROCHET RCROCHET COMMA list_var','list_var',5,'p_list_var','parse.py',88),
  ('bodyexp -> expressions','bodyexp',1,'p_bodyexp','parse.py',92),
  ('roteurexp -> RETOUR expression_op ENDLINE','roteurexp',3,'p_roteurexp','parse.py',100),
  ('expressions -> expression expressions','expressions',2,'p_expressions','parse.py',105),
  ('expressions -> expression_fcall','expressions',1,'p_expressions','parse.py',106),
  ('expressions -> EPSILON','expressions',1,'p_expressions','parse.py',107),
  ('expression -> ID AFFECT expression_fcall','expression',3,'p_expression_affect','parse.py',115),
  ('expression -> ID LCROCHET expression_op RCROCHET AFFECT expression_fcall','expression',6,'p_expression_affect','parse.py',116),
  ('expression -> ID AFFECT expression_op ENDLINE','expression',4,'p_expression_affect','parse.py',117),
  ('expression -> ID LCROCHET expression_op RCROCHET AFFECT expression_op ENDLINE','expression',7,'p_expression_affect','parse.py',118),
  ('expression -> SI comparison_op ALORS LSEPARATEUR expressions RSEPARATEUR SINON LSEPARATEUR expressions RSEPARATEUR','expression',10,'p_expression_si','parse.py',123),
  ('expression -> SI comparison_op ALORS LSEPARATEUR expressions RSEPARATEUR','expression',6,'p_expression_si','parse.py',124),
  ('expression -> TANTQUE comparison_op FAIRE LSEPARATEUR expressions RSEPARATEUR','expression',6,'p_expression_tantque','parse.py',132),
  ('expression -> LIRE LPAREN identifiant RPAREN ENDLINE','expression',5,'p_expression_lire','parse.py',137),
  ('expression -> ECRIRE LPAREN expression_op RPAREN ENDLINE','expression',5,'p_expression_ecrire','parse.py',142),
  ('expression -> ECRIRE LPAREN string_id RPAREN ENDLINE','expression',5,'p_expression_ecrire','parse.py',143),
  ('string_id -> STRING','string_id',1,'p_string_id','parse.py',148),
  ('expression_fcall -> ID LPAREN expression_op RPAREN ENDLINE','expression_fcall',5,'p_expression_fcall','parse.py',153),
  ('expression_fcall -> ID LPAREN string_id RPAREN ENDLINE','expression_fcall',5,'p_expression_fcall','parse.py',154),
  ('expression_fcall -> ID LPAREN RPAREN ENDLINE','expression_fcall',4,'p_expression_fcall','parse.py',155),
  ('expression_op -> expression_op ADD_OP expression_op','expression_op',3,'p_expression_op_entier','parse.py',159),
  ('expression_op -> expression_op MUL_OP expression_op','expression_op',3,'p_expression_op_entier','parse.py',160),
  ('expression_op -> comparison_op','expression_op',1,'p_expression_op_entier','parse.py',161),
  ('comparison_op -> expression_op LOGC_OP expression_op','comparison_op',3,'p_comparison_op','parse.py',169),
  ('comparison_op -> LPAREN comparison_op RPAREN','comparison_op',3,'p_comparison_op_par','parse.py',174),
  ('expression_op -> ID COMMA expression_op','expression_op',3,'p_expression_op_var','parse.py',179),
  ('expression_op -> number COMMA expression_op','expression_op',3,'p_expression_op_var','parse.py',180),
  ('expression_op -> ID','expression_op',1,'p_expression_op_value','parse.py',184),
  ('expression_op -> number','expression_op',1,'p_expression_op_value','parse.py',185),
  ('expression_op -> LPAREN expression_op RPAREN','expression_op',3,'p_expression_op_par','parse.py',190),
  ('number -> ADD_OP NUMBER','number',2,'p_number','parse.py',195),
  ('number -> NUMBER','number',1,'p_number','parse.py',196),
]
