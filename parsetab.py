
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND AS CLOSE_BRACKET CLOSE_PARENTHESIS CLS COMMA DIFFERENT_TO DIM DIVIDE_FLOATING_POINT DIVIDE_ROUND_DOWN DO DOUBLE_POINTS ELSE ELSEIF END EQUALS EQUAL_TO FLOAT FLOAT_VALUE FOR GOSUB GOTO GREATER_OR_EQUAL_THAN GREATER_THAN ID IF INPUT LESS_OR_EQUAL_THAN LESS_THAN LET LOOP MAIN MINUS MOD MULTIPLY NEXT NOT OPEN_BRACKET OPEN_PARENTHESIS OR PLUS POWER_BY PRINT PROCEDURE PROGRAM RETURN SINGLE_POINT STRING SUB THEN TO UNTIL WEND WHILE WORD WORD_VALUE\n\t  MATHSCY  : PROGRAM ID DECLARATIONS PROGRAM_BODY END SINGLE_POINT\n\t\n\t  DECLARATIONS : VARIABLES_DECLARATION SUBPROCEDURES_DECLARATION\n\t\n\t  VARIABLES_DECLARATION : DIM IDS_SEQUENCE AS VARIABLE_TYPE VARIABLES_DECLARATION\n    |\n\t\n\t  IDS_SEQUENCE : ID COMMA IDS_SEQUENCE\n    | ID\n\t\n\t  VARIABLE_TYPE : WORD\n    | WORD DIMENSIONAL_VAR_DECLARATION\n    | FLOAT\n    | FLOAT DIMENSIONAL_VAR_DECLARATION\n\t\n\t  DIMENSIONAL_VAR_DECLARATION : OPEN_BRACKET SIMPLE_VALUE CLOSE_BRACKET\n    | OPEN_BRACKET SIMPLE_VALUE COMMA SIMPLE_VALUE CLOSE_BRACKET\n    | OPEN_BRACKET SIMPLE_VALUE COMMA SIMPLE_VALUE COMMA SIMPLE_VALUE CLOSE_BRACKET\n\t\n\t  SUBPROCEDURES_DECLARATION : SUB PROCEDURE ID STATEMENTS RETURN SUBPROCEDURES_DECLARATION\n    |\n\t\n\t  PROGRAM_BODY : MAIN DOUBLE_POINTS STATEMENTS\n\t\n\t  JUMPERS : GOSUB ID\n    | GOTO ID\n    | ID DOUBLE_POINTS\n\t\n\t  VARIABLE_ASSIGNATION : ID EQUALS ARITHMETIC_EXPRESSION\n    | ID DIMENSIONAL_VAR_INDEX EQUALS ARITHMETIC_EXPRESSION\n    | LET ID EQUALS ARITHMETIC_EXPRESSION\n    | LET ID DIMENSIONAL_VAR_INDEX EQUALS ARITHMETIC_EXPRESSION\n\t\n\t  DIMENSIONAL_VAR_INDEX : OPEN_BRACKET ARITHMETIC_EXPRESSION CLOSE_BRACKET\n    | OPEN_BRACKET ARITHMETIC_EXPRESSION CLOSE_BRACKET OPEN_BRACKET ARITHMETIC_EXPRESSION CLOSE_BRACKET\n    | OPEN_BRACKET ARITHMETIC_EXPRESSION CLOSE_BRACKET OPEN_BRACKET ARITHMETIC_EXPRESSION CLOSE_BRACKET OPEN_BRACKET ARITHMETIC_EXPRESSION CLOSE_BRACKET\n\t\n\t  USER_INTERACTION : CLS\n    | ID EQUALS INPUT OPEN_PARENTHESIS STRINGS_SEQUENCE CLOSE_PARENTHESIS\n    | LET ID EQUALS INPUT OPEN_PARENTHESIS STRINGS_SEQUENCE CLOSE_PARENTHESIS\n    | PRINT OPEN_PARENTHESIS STRINGS_SEQUENCE CLOSE_PARENTHESIS\n\t\n\t  STRINGS_SEQUENCE : STRING COMMA STRINGS_SEQUENCE\n    | STRING\n    | ID COMMA STRINGS_SEQUENCE\n    | ID\n\t\n\t  IF_STATEMENT : IF LOGICAL_EXPRESSION THEN STATEMENTS ELSE_STATEMENT END IF\n\t\n\t  ELSE_STATEMENT : ELSE STATEMENTS\n    | ELSEIF LOGICAL_EXPRESSION THEN STATEMENTS ELSE_STATEMENT\n    |\n\t\n\t  WHILE_STATEMENT : WHILE LOGICAL_EXPRESSION STATEMENTS WEND\n\t\n\t  DO_STATEMENT : DO STATEMENTS LOOP UNTIL LOGICAL_EXPRESSION\n\t\n\t  FOR_STATEMENT : FOR ID EQUALS ARITHMETIC_EXPRESSION TO ARITHMETIC_EXPRESSION SET_FOR_STEPS STATEMENTS NEXT ID\n\t\n\t  SET_FOR_STEPS : OPEN_BRACKET SIMPLE_VALUE CLOSE_BRACKET\n    |\n\t\n\t  STATEMENTS : JUMPERS STATEMENTS\n    | VARIABLE_ASSIGNATION STATEMENTS\n    | USER_INTERACTION STATEMENTS\n    | IF_STATEMENT STATEMENTS\n    | WHILE_STATEMENT STATEMENTS\n    | FOR_STATEMENT STATEMENTS\n    | DO_STATEMENT STATEMENTS\n    |\n\t\n    SIMPLE_VALUE : WORD_VALUE\n    | FLOAT_VALUE\n  \n    ANY_VALUE : SIMPLE_VALUE\n    | ID\n    | ID OPEN_BRACKET ARITHMETIC_EXPRESSION CLOSE_BRACKET\n    | ID OPEN_BRACKET ARITHMETIC_EXPRESSION CLOSE_BRACKET OPEN_BRACKET ARITHMETIC_EXPRESSION CLOSE_BRACKET\n    | ID OPEN_BRACKET ARITHMETIC_EXPRESSION CLOSE_BRACKET OPEN_BRACKET ARITHMETIC_EXPRESSION CLOSE_BRACKET OPEN_BRACKET ARITHMETIC_EXPRESSION CLOSE_BRACKET\n  \n\t  ARITHMETIC_EXPRESSION : ARITHMETIC_EXPRESSION_P1\n    | ARITHMETIC_EXPRESSION PLUS ARITHMETIC_EXPRESSION_P1\n    | ARITHMETIC_EXPRESSION MINUS ARITHMETIC_EXPRESSION_P1\n\t\n\t  ARITHMETIC_EXPRESSION_P1 : ARITHMETIC_EXPRESSION_P2\n    | ARITHMETIC_EXPRESSION_P1 MULTIPLY ARITHMETIC_EXPRESSION_P2\n    | ARITHMETIC_EXPRESSION_P1 DIVIDE_FLOATING_POINT ARITHMETIC_EXPRESSION_P2\n    | ARITHMETIC_EXPRESSION_P1 MOD ARITHMETIC_EXPRESSION_P2\n    | ARITHMETIC_EXPRESSION_P1 DIVIDE_ROUND_DOWN ARITHMETIC_EXPRESSION_P2\n\t\n\t  ARITHMETIC_EXPRESSION_P2 : ARITHMETIC_EXPRESSION_P3\n    | ARITHMETIC_EXPRESSION_P2 POWER_BY ARITHMETIC_EXPRESSION_P3\n\t\n\t  ARITHMETIC_EXPRESSION_P3 : OPEN_PARENTHESIS ARITHMETIC_EXPRESSION CLOSE_PARENTHESIS\n    | ANY_VALUE\n\t\n\t  LOGICAL_EXPRESSION : LOGICAL_EXPRESSION_P1\n    | LOGICAL_EXPRESSION OR LOGICAL_EXPRESSION_P1\n\t\n\t  LOGICAL_EXPRESSION_P1 : LOGICAL_EXPRESSION_P2\n    | LOGICAL_EXPRESSION_P1 AND LOGICAL_EXPRESSION_P2\n\t\n\t  LOGICAL_EXPRESSION_P2 : LOGICAL_EXPRESSION_P3\n    | NOT LOGICAL_EXPRESSION_P3\n\t\n\t  LOGICAL_EXPRESSION_P3 : OPEN_PARENTHESIS LOGICAL_EXPRESSION CLOSE_PARENTHESIS\n    | ARITHMETIC_EXPRESSION RELATIONAL_OPERATOR ARITHMETIC_EXPRESSION\n    \n\t\n\t  RELATIONAL_OPERATOR : EQUAL_TO\n    | DIFFERENT_TO\n    | LESS_THAN\n    | GREATER_THAN\n    | LESS_OR_EQUAL_THAN\n    | GREATER_OR_EQUAL_THAN\n\t'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,18,],[0,-1,]),'ID':([2,6,14,15,17,20,21,22,23,24,25,26,27,29,30,31,33,34,35,36,37,49,50,51,53,54,56,58,59,60,61,62,64,65,66,67,68,69,70,71,72,80,82,83,85,90,91,92,93,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,112,116,118,120,122,123,124,125,127,128,129,130,131,132,133,134,135,136,137,138,140,142,147,148,149,153,154,155,156,157,159,165,166,170,171,172,174,177,179,185,186,187,190,191,],[3,12,28,37,12,28,28,28,28,28,28,28,49,54,55,-27,69,69,73,28,28,-17,-19,69,69,-18,89,-71,-73,-75,69,69,-59,-62,-67,-70,-54,-55,-52,-53,28,-20,69,69,69,28,69,69,-76,69,69,69,-79,-80,-81,-82,-83,-84,69,69,69,69,69,69,69,89,-21,-22,69,-30,89,89,-72,-74,-77,-69,-78,-60,-61,-63,-64,-65,-66,-68,-39,69,69,89,-23,28,69,-56,69,-40,-28,69,-43,-29,-35,28,28,69,-57,69,190,-42,-41,-58,]),'DIM':([3,38,39,40,77,79,144,168,182,],[6,6,-7,-9,-8,-10,-11,-12,-13,]),'SUB':([3,5,38,39,40,76,77,79,114,144,168,182,],[-4,10,-4,-7,-9,-3,-8,-10,10,-11,-12,-13,]),'MAIN':([3,4,5,9,38,39,40,76,77,79,114,143,144,168,182,],[-4,8,-15,-2,-4,-7,-9,-3,-8,-10,-15,-14,-11,-12,-13,]),'END':([7,14,19,20,21,22,23,24,25,26,31,42,43,44,45,46,47,48,49,50,54,58,59,60,64,65,66,67,68,69,70,71,80,90,93,118,120,123,126,127,128,129,130,131,132,133,134,135,136,137,138,140,149,152,153,155,157,159,163,170,171,172,178,179,184,190,191,],[13,-51,-16,-51,-51,-51,-51,-51,-51,-51,-27,-44,-45,-46,-47,-48,-49,-50,-17,-19,-18,-71,-73,-75,-59,-62,-67,-70,-54,-55,-52,-53,-20,-51,-76,-21,-22,-30,-38,-72,-74,-77,-69,-78,-60,-61,-63,-64,-65,-66,-68,-39,-23,162,-51,-56,-40,-28,-36,-29,-35,-51,-38,-57,-37,-41,-58,]),'DOUBLE_POINTS':([8,28,],[14,50,]),'PROCEDURE':([10,],[15,]),'AS':([11,12,41,],[16,-6,-5,]),'COMMA':([12,70,71,88,89,115,158,],[17,-52,-53,124,125,145,167,]),'SINGLE_POINT':([13,],[18,]),'GOSUB':([14,20,21,22,23,24,25,26,31,36,37,49,50,54,58,59,60,64,65,66,67,68,69,70,71,72,80,90,93,118,120,123,127,128,129,130,131,132,133,134,135,136,137,138,140,149,153,155,157,159,166,170,171,172,174,179,187,190,191,],[27,27,27,27,27,27,27,27,-27,27,27,-17,-19,-18,-71,-73,-75,-59,-62,-67,-70,-54,-55,-52,-53,27,-20,27,-76,-21,-22,-30,-72,-74,-77,-69,-78,-60,-61,-63,-64,-65,-66,-68,-39,-23,27,-56,-40,-28,-43,-29,-35,27,27,-57,-42,-41,-58,]),'GOTO':([14,20,21,22,23,24,25,26,31,36,37,49,50,54,58,59,60,64,65,66,67,68,69,70,71,72,80,90,93,118,120,123,127,128,129,130,131,132,133,134,135,136,137,138,140,149,153,155,157,159,166,170,171,172,174,179,187,190,191,],[29,29,29,29,29,29,29,29,-27,29,29,-17,-19,-18,-71,-73,-75,-59,-62,-67,-70,-54,-55,-52,-53,29,-20,29,-76,-21,-22,-30,-72,-74,-77,-69,-78,-60,-61,-63,-64,-65,-66,-68,-39,-23,29,-56,-40,-28,-43,-29,-35,29,29,-57,-42,-41,-58,]),'LET':([14,20,21,22,23,24,25,26,31,36,37,49,50,54,58,59,60,64,65,66,67,68,69,70,71,72,80,90,93,118,120,123,127,128,129,130,131,132,133,134,135,136,137,138,140,149,153,155,157,159,166,170,171,172,174,179,187,190,191,],[30,30,30,30,30,30,30,30,-27,30,30,-17,-19,-18,-71,-73,-75,-59,-62,-67,-70,-54,-55,-52,-53,30,-20,30,-76,-21,-22,-30,-72,-74,-77,-69,-78,-60,-61,-63,-64,-65,-66,-68,-39,-23,30,-56,-40,-28,-43,-29,-35,30,30,-57,-42,-41,-58,]),'CLS':([14,20,21,22,23,24,25,26,31,36,37,49,50,54,58,59,60,64,65,66,67,68,69,70,71,72,80,90,93,118,120,123,127,128,129,130,131,132,133,134,135,136,137,138,140,149,153,155,157,159,166,170,171,172,174,179,187,190,191,],[31,31,31,31,31,31,31,31,-27,31,31,-17,-19,-18,-71,-73,-75,-59,-62,-67,-70,-54,-55,-52,-53,31,-20,31,-76,-21,-22,-30,-72,-74,-77,-69,-78,-60,-61,-63,-64,-65,-66,-68,-39,-23,31,-56,-40,-28,-43,-29,-35,31,31,-57,-42,-41,-58,]),'PRINT':([14,20,21,22,23,24,25,26,31,36,37,49,50,54,58,59,60,64,65,66,67,68,69,70,71,72,80,90,93,118,120,123,127,128,129,130,131,132,133,134,135,136,137,138,140,149,153,155,157,159,166,170,171,172,174,179,187,190,191,],[32,32,32,32,32,32,32,32,-27,32,32,-17,-19,-18,-71,-73,-75,-59,-62,-67,-70,-54,-55,-52,-53,32,-20,32,-76,-21,-22,-30,-72,-74,-77,-69,-78,-60,-61,-63,-64,-65,-66,-68,-39,-23,32,-56,-40,-28,-43,-29,-35,32,32,-57,-42,-41,-58,]),'IF':([14,20,21,22,23,24,25,26,31,36,37,49,50,54,58,59,60,64,65,66,67,68,69,70,71,72,80,90,93,118,120,123,127,128,129,130,131,132,133,134,135,136,137,138,140,149,153,155,157,159,162,166,170,171,172,174,179,187,190,191,],[33,33,33,33,33,33,33,33,-27,33,33,-17,-19,-18,-71,-73,-75,-59,-62,-67,-70,-54,-55,-52,-53,33,-20,33,-76,-21,-22,-30,-72,-74,-77,-69,-78,-60,-61,-63,-64,-65,-66,-68,-39,-23,33,-56,-40,-28,171,-43,-29,-35,33,33,-57,-42,-41,-58,]),'WHILE':([14,20,21,22,23,24,25,26,31,36,37,49,50,54,58,59,60,64,65,66,67,68,69,70,71,72,80,90,93,118,120,123,127,128,129,130,131,132,133,134,135,136,137,138,140,149,153,155,157,159,166,170,171,172,174,179,187,190,191,],[34,34,34,34,34,34,34,34,-27,34,34,-17,-19,-18,-71,-73,-75,-59,-62,-67,-70,-54,-55,-52,-53,34,-20,34,-76,-21,-22,-30,-72,-74,-77,-69,-78,-60,-61,-63,-64,-65,-66,-68,-39,-23,34,-56,-40,-28,-43,-29,-35,34,34,-57,-42,-41,-58,]),'FOR':([14,20,21,22,23,24,25,26,31,36,37,49,50,54,58,59,60,64,65,66,67,68,69,70,71,72,80,90,93,118,120,123,127,128,129,130,131,132,133,134,135,136,137,138,140,149,153,155,157,159,166,170,171,172,174,179,187,190,191,],[35,35,35,35,35,35,35,35,-27,35,35,-17,-19,-18,-71,-73,-75,-59,-62,-67,-70,-54,-55,-52,-53,35,-20,35,-76,-21,-22,-30,-72,-74,-77,-69,-78,-60,-61,-63,-64,-65,-66,-68,-39,-23,35,-56,-40,-28,-43,-29,-35,35,35,-57,-42,-41,-58,]),'DO':([14,20,21,22,23,24,25,26,31,36,37,49,50,54,58,59,60,64,65,66,67,68,69,70,71,72,80,90,93,118,120,123,127,128,129,130,131,132,133,134,135,136,137,138,140,149,153,155,157,159,166,170,171,172,174,179,187,190,191,],[36,36,36,36,36,36,36,36,-27,36,36,-17,-19,-18,-71,-73,-75,-59,-62,-67,-70,-54,-55,-52,-53,36,-20,36,-76,-21,-22,-30,-72,-74,-77,-69,-78,-60,-61,-63,-64,-65,-66,-68,-39,-23,36,-56,-40,-28,-43,-29,-35,36,36,-57,-42,-41,-58,]),'WORD':([16,],[39,]),'FLOAT':([16,],[40,]),'LOOP':([20,21,22,23,24,25,26,31,36,42,43,44,45,46,47,48,49,50,54,58,59,60,64,65,66,67,68,69,70,71,74,80,93,118,120,123,127,128,129,130,131,132,133,134,135,136,137,138,140,149,155,157,159,170,171,179,190,191,],[-51,-51,-51,-51,-51,-51,-51,-27,-51,-44,-45,-46,-47,-48,-49,-50,-17,-19,-18,-71,-73,-75,-59,-62,-67,-70,-54,-55,-52,-53,113,-20,-76,-21,-22,-30,-72,-74,-77,-69,-78,-60,-61,-63,-64,-65,-66,-68,-39,-23,-56,-40,-28,-29,-35,-57,-41,-58,]),'RETURN':([20,21,22,23,24,25,26,31,37,42,43,44,45,46,47,48,49,50,54,58,59,60,64,65,66,67,68,69,70,71,75,80,93,118,120,123,127,128,129,130,131,132,133,134,135,136,137,138,140,149,155,157,159,170,171,179,190,191,],[-51,-51,-51,-51,-51,-51,-51,-27,-51,-44,-45,-46,-47,-48,-49,-50,-17,-19,-18,-71,-73,-75,-59,-62,-67,-70,-54,-55,-52,-53,114,-20,-76,-21,-22,-30,-72,-74,-77,-69,-78,-60,-61,-63,-64,-65,-66,-68,-39,-23,-56,-40,-28,-29,-35,-57,-41,-58,]),'WEND':([20,21,22,23,24,25,26,31,42,43,44,45,46,47,48,49,50,54,58,59,60,64,65,66,67,68,69,70,71,72,80,93,111,118,120,123,127,128,129,130,131,132,133,134,135,136,137,138,140,149,155,157,159,170,171,179,190,191,],[-51,-51,-51,-51,-51,-51,-51,-27,-44,-45,-46,-47,-48,-49,-50,-17,-19,-18,-71,-73,-75,-59,-62,-67,-70,-54,-55,-52,-53,-51,-20,-76,140,-21,-22,-30,-72,-74,-77,-69,-78,-60,-61,-63,-64,-65,-66,-68,-39,-23,-56,-40,-28,-29,-35,-57,-41,-58,]),'ELSE':([20,21,22,23,24,25,26,31,42,43,44,45,46,47,48,49,50,54,58,59,60,64,65,66,67,68,69,70,71,80,90,93,118,120,123,126,127,128,129,130,131,132,133,134,135,136,137,138,140,149,155,157,159,170,171,172,178,179,190,191,],[-51,-51,-51,-51,-51,-51,-51,-27,-44,-45,-46,-47,-48,-49,-50,-17,-19,-18,-71,-73,-75,-59,-62,-67,-70,-54,-55,-52,-53,-20,-51,-76,-21,-22,-30,153,-72,-74,-77,-69,-78,-60,-61,-63,-64,-65,-66,-68,-39,-23,-56,-40,-28,-29,-35,-51,153,-57,-41,-58,]),'ELSEIF':([20,21,22,23,24,25,26,31,42,43,44,45,46,47,48,49,50,54,58,59,60,64,65,66,67,68,69,70,71,80,90,93,118,120,123,126,127,128,129,130,131,132,133,134,135,136,137,138,140,149,155,157,159,170,171,172,178,179,190,191,],[-51,-51,-51,-51,-51,-51,-51,-27,-44,-45,-46,-47,-48,-49,-50,-17,-19,-18,-71,-73,-75,-59,-62,-67,-70,-54,-55,-52,-53,-20,-51,-76,-21,-22,-30,154,-72,-74,-77,-69,-78,-60,-61,-63,-64,-65,-66,-68,-39,-23,-56,-40,-28,-29,-35,-51,154,-57,-41,-58,]),'NEXT':([20,21,22,23,24,25,26,31,42,43,44,45,46,47,48,49,50,54,58,59,60,64,65,66,67,68,69,70,71,80,93,118,120,123,127,128,129,130,131,132,133,134,135,136,137,138,140,149,155,157,159,166,170,171,174,179,180,187,190,191,],[-51,-51,-51,-51,-51,-51,-51,-27,-44,-45,-46,-47,-48,-49,-50,-17,-19,-18,-71,-73,-75,-59,-62,-67,-70,-54,-55,-52,-53,-20,-76,-21,-22,-30,-72,-74,-77,-69,-78,-60,-61,-63,-64,-65,-66,-68,-39,-23,-56,-40,-28,-43,-29,-35,-51,-57,186,-42,-41,-58,]),'EQUALS':([28,52,55,73,86,119,169,188,],[51,83,85,112,122,-24,-25,-26,]),'OPEN_BRACKET':([28,39,40,55,64,65,66,67,68,69,70,71,119,130,132,133,134,135,136,137,138,155,166,169,179,191,],[53,78,78,53,-59,-62,-67,-70,-54,110,-52,-53,147,-69,-60,-61,-63,-64,-65,-66,-68,165,175,177,185,-58,]),'OPEN_PARENTHESIS':([32,33,34,51,53,61,62,81,82,83,85,91,92,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,112,121,122,142,147,154,156,165,177,185,],[56,62,62,82,82,62,62,116,82,82,82,62,62,82,82,82,-79,-80,-81,-82,-83,-84,82,82,82,82,82,82,82,148,82,62,82,62,82,82,82,82,]),'NOT':([33,34,62,91,92,142,154,],[61,61,61,61,61,61,61,]),'WORD_VALUE':([33,34,51,53,61,62,78,82,83,85,91,92,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,112,122,142,145,147,154,156,165,167,175,177,185,],[70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,-79,-80,-81,-82,-83,-84,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,]),'FLOAT_VALUE':([33,34,51,53,61,62,78,82,83,85,91,92,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,112,122,142,145,147,154,156,165,167,175,177,185,],[71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,-79,-80,-81,-82,-83,-84,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,]),'INPUT':([51,85,],[81,121,]),'STRING':([56,116,124,125,148,],[88,88,88,88,88,]),'THEN':([57,58,59,60,64,65,66,67,68,69,70,71,93,127,128,129,130,131,132,133,134,135,136,137,138,155,164,179,191,],[90,-71,-73,-75,-59,-62,-67,-70,-54,-55,-52,-53,-76,-72,-74,-77,-69,-78,-60,-61,-63,-64,-65,-66,-68,-56,172,-57,-58,]),'OR':([57,58,59,60,64,65,66,67,68,69,70,71,72,93,94,127,128,129,130,131,132,133,134,135,136,137,138,155,157,164,179,191,],[91,-71,-73,-75,-59,-62,-67,-70,-54,-55,-52,-53,91,-76,91,-72,-74,-77,-69,-78,-60,-61,-63,-64,-65,-66,-68,-56,91,91,-57,-58,]),'CLOSE_PARENTHESIS':([58,59,60,64,65,66,67,68,69,70,71,87,88,89,93,94,95,117,127,128,129,130,131,132,133,134,135,136,137,138,146,150,151,155,161,179,191,],[-71,-73,-75,-59,-62,-67,-70,-54,-55,-52,-53,123,-32,-34,-76,129,130,130,-72,-74,-77,-69,-78,-60,-61,-63,-64,-65,-66,-68,159,-31,-33,-56,170,-57,-58,]),'AND':([58,59,60,64,65,66,67,68,69,70,71,93,127,128,129,130,131,132,133,134,135,136,137,138,155,179,191,],[92,-73,-75,-59,-62,-67,-70,-54,-55,-52,-53,-76,92,-74,-77,-69,-78,-60,-61,-63,-64,-65,-66,-68,-56,-57,-58,]),'PLUS':([63,64,65,66,67,68,69,70,71,80,84,95,117,118,120,130,131,132,133,134,135,136,137,138,139,141,149,155,160,166,173,179,183,189,191,],[97,-59,-62,-67,-70,-54,-55,-52,-53,97,97,97,97,97,97,-69,97,-60,-61,-63,-64,-65,-66,-68,97,97,97,-56,97,97,97,-57,97,97,-58,]),'MINUS':([63,64,65,66,67,68,69,70,71,80,84,95,117,118,120,130,131,132,133,134,135,136,137,138,139,141,149,155,160,166,173,179,183,189,191,],[98,-59,-62,-67,-70,-54,-55,-52,-53,98,98,98,98,98,98,-69,98,-60,-61,-63,-64,-65,-66,-68,98,98,98,-56,98,98,98,-57,98,98,-58,]),'EQUAL_TO':([63,64,65,66,67,68,69,70,71,95,130,132,133,134,135,136,137,138,155,179,191,],[99,-59,-62,-67,-70,-54,-55,-52,-53,99,-69,-60,-61,-63,-64,-65,-66,-68,-56,-57,-58,]),'DIFFERENT_TO':([63,64,65,66,67,68,69,70,71,95,130,132,133,134,135,136,137,138,155,179,191,],[100,-59,-62,-67,-70,-54,-55,-52,-53,100,-69,-60,-61,-63,-64,-65,-66,-68,-56,-57,-58,]),'LESS_THAN':([63,64,65,66,67,68,69,70,71,95,130,132,133,134,135,136,137,138,155,179,191,],[101,-59,-62,-67,-70,-54,-55,-52,-53,101,-69,-60,-61,-63,-64,-65,-66,-68,-56,-57,-58,]),'GREATER_THAN':([63,64,65,66,67,68,69,70,71,95,130,132,133,134,135,136,137,138,155,179,191,],[102,-59,-62,-67,-70,-54,-55,-52,-53,102,-69,-60,-61,-63,-64,-65,-66,-68,-56,-57,-58,]),'LESS_OR_EQUAL_THAN':([63,64,65,66,67,68,69,70,71,95,130,132,133,134,135,136,137,138,155,179,191,],[103,-59,-62,-67,-70,-54,-55,-52,-53,103,-69,-60,-61,-63,-64,-65,-66,-68,-56,-57,-58,]),'GREATER_OR_EQUAL_THAN':([63,64,65,66,67,68,69,70,71,95,130,132,133,134,135,136,137,138,155,179,191,],[104,-59,-62,-67,-70,-54,-55,-52,-53,104,-69,-60,-61,-63,-64,-65,-66,-68,-56,-57,-58,]),'CLOSE_BRACKET':([64,65,66,67,68,69,70,71,84,115,130,132,133,134,135,136,137,138,139,155,158,160,173,176,179,181,183,189,191,],[-59,-62,-67,-70,-54,-55,-52,-53,119,144,-69,-60,-61,-63,-64,-65,-66,-68,155,-56,168,169,179,182,-57,187,188,191,-58,]),'TO':([64,65,66,67,68,69,70,71,130,132,133,134,135,136,137,138,141,155,179,191,],[-59,-62,-67,-70,-54,-55,-52,-53,-69,-60,-61,-63,-64,-65,-66,-68,156,-56,-57,-58,]),'MULTIPLY':([64,65,66,67,68,69,70,71,130,132,133,134,135,136,137,138,155,179,191,],[105,-62,-67,-70,-54,-55,-52,-53,-69,105,105,-63,-64,-65,-66,-68,-56,-57,-58,]),'DIVIDE_FLOATING_POINT':([64,65,66,67,68,69,70,71,130,132,133,134,135,136,137,138,155,179,191,],[106,-62,-67,-70,-54,-55,-52,-53,-69,106,106,-63,-64,-65,-66,-68,-56,-57,-58,]),'MOD':([64,65,66,67,68,69,70,71,130,132,133,134,135,136,137,138,155,179,191,],[107,-62,-67,-70,-54,-55,-52,-53,-69,107,107,-63,-64,-65,-66,-68,-56,-57,-58,]),'DIVIDE_ROUND_DOWN':([64,65,66,67,68,69,70,71,130,132,133,134,135,136,137,138,155,179,191,],[108,-62,-67,-70,-54,-55,-52,-53,-69,108,108,-63,-64,-65,-66,-68,-56,-57,-58,]),'POWER_BY':([65,66,67,68,69,70,71,130,134,135,136,137,138,155,179,191,],[109,-67,-70,-54,-55,-52,-53,-69,109,109,109,109,-68,-56,-57,-58,]),'UNTIL':([113,],[142,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'MATHSCY':([0,],[1,]),'DECLARATIONS':([3,],[4,]),'VARIABLES_DECLARATION':([3,38,],[5,76,]),'PROGRAM_BODY':([4,],[7,]),'SUBPROCEDURES_DECLARATION':([5,114,],[9,143,]),'IDS_SEQUENCE':([6,17,],[11,41,]),'STATEMENTS':([14,20,21,22,23,24,25,26,36,37,72,90,153,172,174,],[19,42,43,44,45,46,47,48,74,75,111,126,163,178,180,]),'JUMPERS':([14,20,21,22,23,24,25,26,36,37,72,90,153,172,174,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'VARIABLE_ASSIGNATION':([14,20,21,22,23,24,25,26,36,37,72,90,153,172,174,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'USER_INTERACTION':([14,20,21,22,23,24,25,26,36,37,72,90,153,172,174,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'IF_STATEMENT':([14,20,21,22,23,24,25,26,36,37,72,90,153,172,174,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'WHILE_STATEMENT':([14,20,21,22,23,24,25,26,36,37,72,90,153,172,174,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'FOR_STATEMENT':([14,20,21,22,23,24,25,26,36,37,72,90,153,172,174,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'DO_STATEMENT':([14,20,21,22,23,24,25,26,36,37,72,90,153,172,174,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'VARIABLE_TYPE':([16,],[38,]),'DIMENSIONAL_VAR_INDEX':([28,55,],[52,86,]),'LOGICAL_EXPRESSION':([33,34,62,142,154,],[57,72,94,157,164,]),'LOGICAL_EXPRESSION_P1':([33,34,62,91,142,154,],[58,58,58,127,58,58,]),'LOGICAL_EXPRESSION_P2':([33,34,62,91,92,142,154,],[59,59,59,59,128,59,59,]),'LOGICAL_EXPRESSION_P3':([33,34,61,62,91,92,142,154,],[60,60,93,60,60,60,60,60,]),'ARITHMETIC_EXPRESSION':([33,34,51,53,61,62,82,83,85,91,92,96,110,112,122,142,147,154,156,165,177,185,],[63,63,80,84,63,95,117,118,120,63,63,131,139,141,149,63,160,63,166,173,183,189,]),'ARITHMETIC_EXPRESSION_P1':([33,34,51,53,61,62,82,83,85,91,92,96,97,98,110,112,122,142,147,154,156,165,177,185,],[64,64,64,64,64,64,64,64,64,64,64,64,132,133,64,64,64,64,64,64,64,64,64,64,]),'ARITHMETIC_EXPRESSION_P2':([33,34,51,53,61,62,82,83,85,91,92,96,97,98,105,106,107,108,110,112,122,142,147,154,156,165,177,185,],[65,65,65,65,65,65,65,65,65,65,65,65,65,65,134,135,136,137,65,65,65,65,65,65,65,65,65,65,]),'ARITHMETIC_EXPRESSION_P3':([33,34,51,53,61,62,82,83,85,91,92,96,97,98,105,106,107,108,109,110,112,122,142,147,154,156,165,177,185,],[66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,138,66,66,66,66,66,66,66,66,66,66,]),'ANY_VALUE':([33,34,51,53,61,62,82,83,85,91,92,96,97,98,105,106,107,108,109,110,112,122,142,147,154,156,165,177,185,],[67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,]),'SIMPLE_VALUE':([33,34,51,53,61,62,78,82,83,85,91,92,96,97,98,105,106,107,108,109,110,112,122,142,145,147,154,156,165,167,175,177,185,],[68,68,68,68,68,68,115,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,158,68,68,68,68,176,181,68,68,]),'DIMENSIONAL_VAR_DECLARATION':([39,40,],[77,79,]),'STRINGS_SEQUENCE':([56,116,124,125,148,],[87,146,150,151,161,]),'RELATIONAL_OPERATOR':([63,95,],[96,96,]),'ELSE_STATEMENT':([126,178,],[152,184,]),'SET_FOR_STEPS':([166,],[174,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> MATHSCY","S'",1,None,None,None),
  ('MATHSCY -> PROGRAM ID DECLARATIONS PROGRAM_BODY END SINGLE_POINT','MATHSCY',6,'p_MATHSCY','AnalizadorLexico&SIntaxis.py',105),
  ('DECLARATIONS -> VARIABLES_DECLARATION SUBPROCEDURES_DECLARATION','DECLARATIONS',2,'p_DECLARATIONS','AnalizadorLexico&SIntaxis.py',111),
  ('VARIABLES_DECLARATION -> DIM IDS_SEQUENCE AS VARIABLE_TYPE VARIABLES_DECLARATION','VARIABLES_DECLARATION',5,'p_VARIABLES_DECLARATION','AnalizadorLexico&SIntaxis.py',115),
  ('VARIABLES_DECLARATION -> <empty>','VARIABLES_DECLARATION',0,'p_VARIABLES_DECLARATION','AnalizadorLexico&SIntaxis.py',116),
  ('IDS_SEQUENCE -> ID COMMA IDS_SEQUENCE','IDS_SEQUENCE',3,'p_IDS_SEQUENCE','AnalizadorLexico&SIntaxis.py',123),
  ('IDS_SEQUENCE -> ID','IDS_SEQUENCE',1,'p_IDS_SEQUENCE','AnalizadorLexico&SIntaxis.py',124),
  ('VARIABLE_TYPE -> WORD','VARIABLE_TYPE',1,'p_VARIABLE_TYPE','AnalizadorLexico&SIntaxis.py',135),
  ('VARIABLE_TYPE -> WORD DIMENSIONAL_VAR_DECLARATION','VARIABLE_TYPE',2,'p_VARIABLE_TYPE','AnalizadorLexico&SIntaxis.py',136),
  ('VARIABLE_TYPE -> FLOAT','VARIABLE_TYPE',1,'p_VARIABLE_TYPE','AnalizadorLexico&SIntaxis.py',137),
  ('VARIABLE_TYPE -> FLOAT DIMENSIONAL_VAR_DECLARATION','VARIABLE_TYPE',2,'p_VARIABLE_TYPE','AnalizadorLexico&SIntaxis.py',138),
  ('DIMENSIONAL_VAR_DECLARATION -> OPEN_BRACKET SIMPLE_VALUE CLOSE_BRACKET','DIMENSIONAL_VAR_DECLARATION',3,'p_DIMENSIONAL_VAR_DECLARATION','AnalizadorLexico&SIntaxis.py',150),
  ('DIMENSIONAL_VAR_DECLARATION -> OPEN_BRACKET SIMPLE_VALUE COMMA SIMPLE_VALUE CLOSE_BRACKET','DIMENSIONAL_VAR_DECLARATION',5,'p_DIMENSIONAL_VAR_DECLARATION','AnalizadorLexico&SIntaxis.py',151),
  ('DIMENSIONAL_VAR_DECLARATION -> OPEN_BRACKET SIMPLE_VALUE COMMA SIMPLE_VALUE COMMA SIMPLE_VALUE CLOSE_BRACKET','DIMENSIONAL_VAR_DECLARATION',7,'p_DIMENSIONAL_VAR_DECLARATION','AnalizadorLexico&SIntaxis.py',152),
  ('SUBPROCEDURES_DECLARATION -> SUB PROCEDURE ID STATEMENTS RETURN SUBPROCEDURES_DECLARATION','SUBPROCEDURES_DECLARATION',6,'p_SUBPROCEDURES_DECLARATION','AnalizadorLexico&SIntaxis.py',156),
  ('SUBPROCEDURES_DECLARATION -> <empty>','SUBPROCEDURES_DECLARATION',0,'p_SUBPROCEDURES_DECLARATION','AnalizadorLexico&SIntaxis.py',157),
  ('PROGRAM_BODY -> MAIN DOUBLE_POINTS STATEMENTS','PROGRAM_BODY',3,'p_PROGRAM_BODY','AnalizadorLexico&SIntaxis.py',162),
  ('JUMPERS -> GOSUB ID','JUMPERS',2,'p_JUMPERS','AnalizadorLexico&SIntaxis.py',167),
  ('JUMPERS -> GOTO ID','JUMPERS',2,'p_JUMPERS','AnalizadorLexico&SIntaxis.py',168),
  ('JUMPERS -> ID DOUBLE_POINTS','JUMPERS',2,'p_JUMPERS','AnalizadorLexico&SIntaxis.py',169),
  ('VARIABLE_ASSIGNATION -> ID EQUALS ARITHMETIC_EXPRESSION','VARIABLE_ASSIGNATION',3,'p_VARIABLE_ASSIGNATION','AnalizadorLexico&SIntaxis.py',174),
  ('VARIABLE_ASSIGNATION -> ID DIMENSIONAL_VAR_INDEX EQUALS ARITHMETIC_EXPRESSION','VARIABLE_ASSIGNATION',4,'p_VARIABLE_ASSIGNATION','AnalizadorLexico&SIntaxis.py',175),
  ('VARIABLE_ASSIGNATION -> LET ID EQUALS ARITHMETIC_EXPRESSION','VARIABLE_ASSIGNATION',4,'p_VARIABLE_ASSIGNATION','AnalizadorLexico&SIntaxis.py',176),
  ('VARIABLE_ASSIGNATION -> LET ID DIMENSIONAL_VAR_INDEX EQUALS ARITHMETIC_EXPRESSION','VARIABLE_ASSIGNATION',5,'p_VARIABLE_ASSIGNATION','AnalizadorLexico&SIntaxis.py',177),
  ('DIMENSIONAL_VAR_INDEX -> OPEN_BRACKET ARITHMETIC_EXPRESSION CLOSE_BRACKET','DIMENSIONAL_VAR_INDEX',3,'p_DIMENSIONAL_VAR_INDEX','AnalizadorLexico&SIntaxis.py',182),
  ('DIMENSIONAL_VAR_INDEX -> OPEN_BRACKET ARITHMETIC_EXPRESSION CLOSE_BRACKET OPEN_BRACKET ARITHMETIC_EXPRESSION CLOSE_BRACKET','DIMENSIONAL_VAR_INDEX',6,'p_DIMENSIONAL_VAR_INDEX','AnalizadorLexico&SIntaxis.py',183),
  ('DIMENSIONAL_VAR_INDEX -> OPEN_BRACKET ARITHMETIC_EXPRESSION CLOSE_BRACKET OPEN_BRACKET ARITHMETIC_EXPRESSION CLOSE_BRACKET OPEN_BRACKET ARITHMETIC_EXPRESSION CLOSE_BRACKET','DIMENSIONAL_VAR_INDEX',9,'p_DIMENSIONAL_VAR_INDEX','AnalizadorLexico&SIntaxis.py',184),
  ('USER_INTERACTION -> CLS','USER_INTERACTION',1,'p_USER_INTERACTION','AnalizadorLexico&SIntaxis.py',189),
  ('USER_INTERACTION -> ID EQUALS INPUT OPEN_PARENTHESIS STRINGS_SEQUENCE CLOSE_PARENTHESIS','USER_INTERACTION',6,'p_USER_INTERACTION','AnalizadorLexico&SIntaxis.py',190),
  ('USER_INTERACTION -> LET ID EQUALS INPUT OPEN_PARENTHESIS STRINGS_SEQUENCE CLOSE_PARENTHESIS','USER_INTERACTION',7,'p_USER_INTERACTION','AnalizadorLexico&SIntaxis.py',191),
  ('USER_INTERACTION -> PRINT OPEN_PARENTHESIS STRINGS_SEQUENCE CLOSE_PARENTHESIS','USER_INTERACTION',4,'p_USER_INTERACTION','AnalizadorLexico&SIntaxis.py',192),
  ('STRINGS_SEQUENCE -> STRING COMMA STRINGS_SEQUENCE','STRINGS_SEQUENCE',3,'p_STRINGS_SEQUENCE','AnalizadorLexico&SIntaxis.py',196),
  ('STRINGS_SEQUENCE -> STRING','STRINGS_SEQUENCE',1,'p_STRINGS_SEQUENCE','AnalizadorLexico&SIntaxis.py',197),
  ('STRINGS_SEQUENCE -> ID COMMA STRINGS_SEQUENCE','STRINGS_SEQUENCE',3,'p_STRINGS_SEQUENCE','AnalizadorLexico&SIntaxis.py',198),
  ('STRINGS_SEQUENCE -> ID','STRINGS_SEQUENCE',1,'p_STRINGS_SEQUENCE','AnalizadorLexico&SIntaxis.py',199),
  ('IF_STATEMENT -> IF LOGICAL_EXPRESSION THEN STATEMENTS ELSE_STATEMENT END IF','IF_STATEMENT',7,'p_IF_STATEMENT','AnalizadorLexico&SIntaxis.py',204),
  ('ELSE_STATEMENT -> ELSE STATEMENTS','ELSE_STATEMENT',2,'p_ELSE_STATEMENT','AnalizadorLexico&SIntaxis.py',208),
  ('ELSE_STATEMENT -> ELSEIF LOGICAL_EXPRESSION THEN STATEMENTS ELSE_STATEMENT','ELSE_STATEMENT',5,'p_ELSE_STATEMENT','AnalizadorLexico&SIntaxis.py',209),
  ('ELSE_STATEMENT -> <empty>','ELSE_STATEMENT',0,'p_ELSE_STATEMENT','AnalizadorLexico&SIntaxis.py',210),
  ('WHILE_STATEMENT -> WHILE LOGICAL_EXPRESSION STATEMENTS WEND','WHILE_STATEMENT',4,'p_WHILE_STATEMENT','AnalizadorLexico&SIntaxis.py',215),
  ('DO_STATEMENT -> DO STATEMENTS LOOP UNTIL LOGICAL_EXPRESSION','DO_STATEMENT',5,'p_DO_STATEMENT','AnalizadorLexico&SIntaxis.py',220),
  ('FOR_STATEMENT -> FOR ID EQUALS ARITHMETIC_EXPRESSION TO ARITHMETIC_EXPRESSION SET_FOR_STEPS STATEMENTS NEXT ID','FOR_STATEMENT',10,'p_FOR_STATEMENT','AnalizadorLexico&SIntaxis.py',225),
  ('SET_FOR_STEPS -> OPEN_BRACKET SIMPLE_VALUE CLOSE_BRACKET','SET_FOR_STEPS',3,'p_SET_FOR_STEPS','AnalizadorLexico&SIntaxis.py',229),
  ('SET_FOR_STEPS -> <empty>','SET_FOR_STEPS',0,'p_SET_FOR_STEPS','AnalizadorLexico&SIntaxis.py',230),
  ('STATEMENTS -> JUMPERS STATEMENTS','STATEMENTS',2,'p_STATEMENTS','AnalizadorLexico&SIntaxis.py',235),
  ('STATEMENTS -> VARIABLE_ASSIGNATION STATEMENTS','STATEMENTS',2,'p_STATEMENTS','AnalizadorLexico&SIntaxis.py',236),
  ('STATEMENTS -> USER_INTERACTION STATEMENTS','STATEMENTS',2,'p_STATEMENTS','AnalizadorLexico&SIntaxis.py',237),
  ('STATEMENTS -> IF_STATEMENT STATEMENTS','STATEMENTS',2,'p_STATEMENTS','AnalizadorLexico&SIntaxis.py',238),
  ('STATEMENTS -> WHILE_STATEMENT STATEMENTS','STATEMENTS',2,'p_STATEMENTS','AnalizadorLexico&SIntaxis.py',239),
  ('STATEMENTS -> FOR_STATEMENT STATEMENTS','STATEMENTS',2,'p_STATEMENTS','AnalizadorLexico&SIntaxis.py',240),
  ('STATEMENTS -> DO_STATEMENT STATEMENTS','STATEMENTS',2,'p_STATEMENTS','AnalizadorLexico&SIntaxis.py',241),
  ('STATEMENTS -> <empty>','STATEMENTS',0,'p_STATEMENTS','AnalizadorLexico&SIntaxis.py',242),
  ('SIMPLE_VALUE -> WORD_VALUE','SIMPLE_VALUE',1,'p_SIMPLE_VALUE','AnalizadorLexico&SIntaxis.py',248),
  ('SIMPLE_VALUE -> FLOAT_VALUE','SIMPLE_VALUE',1,'p_SIMPLE_VALUE','AnalizadorLexico&SIntaxis.py',249),
  ('ANY_VALUE -> SIMPLE_VALUE','ANY_VALUE',1,'p_ANY_VALUE','AnalizadorLexico&SIntaxis.py',254),
  ('ANY_VALUE -> ID','ANY_VALUE',1,'p_ANY_VALUE','AnalizadorLexico&SIntaxis.py',255),
  ('ANY_VALUE -> ID OPEN_BRACKET ARITHMETIC_EXPRESSION CLOSE_BRACKET','ANY_VALUE',4,'p_ANY_VALUE','AnalizadorLexico&SIntaxis.py',256),
  ('ANY_VALUE -> ID OPEN_BRACKET ARITHMETIC_EXPRESSION CLOSE_BRACKET OPEN_BRACKET ARITHMETIC_EXPRESSION CLOSE_BRACKET','ANY_VALUE',7,'p_ANY_VALUE','AnalizadorLexico&SIntaxis.py',257),
  ('ANY_VALUE -> ID OPEN_BRACKET ARITHMETIC_EXPRESSION CLOSE_BRACKET OPEN_BRACKET ARITHMETIC_EXPRESSION CLOSE_BRACKET OPEN_BRACKET ARITHMETIC_EXPRESSION CLOSE_BRACKET','ANY_VALUE',10,'p_ANY_VALUE','AnalizadorLexico&SIntaxis.py',258),
  ('ARITHMETIC_EXPRESSION -> ARITHMETIC_EXPRESSION_P1','ARITHMETIC_EXPRESSION',1,'p_ARITHMETIC_EXPRESSION','AnalizadorLexico&SIntaxis.py',264),
  ('ARITHMETIC_EXPRESSION -> ARITHMETIC_EXPRESSION PLUS ARITHMETIC_EXPRESSION_P1','ARITHMETIC_EXPRESSION',3,'p_ARITHMETIC_EXPRESSION','AnalizadorLexico&SIntaxis.py',265),
  ('ARITHMETIC_EXPRESSION -> ARITHMETIC_EXPRESSION MINUS ARITHMETIC_EXPRESSION_P1','ARITHMETIC_EXPRESSION',3,'p_ARITHMETIC_EXPRESSION','AnalizadorLexico&SIntaxis.py',266),
  ('ARITHMETIC_EXPRESSION_P1 -> ARITHMETIC_EXPRESSION_P2','ARITHMETIC_EXPRESSION_P1',1,'p_ARITHMETIC_EXPRESSION_P1','AnalizadorLexico&SIntaxis.py',270),
  ('ARITHMETIC_EXPRESSION_P1 -> ARITHMETIC_EXPRESSION_P1 MULTIPLY ARITHMETIC_EXPRESSION_P2','ARITHMETIC_EXPRESSION_P1',3,'p_ARITHMETIC_EXPRESSION_P1','AnalizadorLexico&SIntaxis.py',271),
  ('ARITHMETIC_EXPRESSION_P1 -> ARITHMETIC_EXPRESSION_P1 DIVIDE_FLOATING_POINT ARITHMETIC_EXPRESSION_P2','ARITHMETIC_EXPRESSION_P1',3,'p_ARITHMETIC_EXPRESSION_P1','AnalizadorLexico&SIntaxis.py',272),
  ('ARITHMETIC_EXPRESSION_P1 -> ARITHMETIC_EXPRESSION_P1 MOD ARITHMETIC_EXPRESSION_P2','ARITHMETIC_EXPRESSION_P1',3,'p_ARITHMETIC_EXPRESSION_P1','AnalizadorLexico&SIntaxis.py',273),
  ('ARITHMETIC_EXPRESSION_P1 -> ARITHMETIC_EXPRESSION_P1 DIVIDE_ROUND_DOWN ARITHMETIC_EXPRESSION_P2','ARITHMETIC_EXPRESSION_P1',3,'p_ARITHMETIC_EXPRESSION_P1','AnalizadorLexico&SIntaxis.py',274),
  ('ARITHMETIC_EXPRESSION_P2 -> ARITHMETIC_EXPRESSION_P3','ARITHMETIC_EXPRESSION_P2',1,'p_ARITHMETIC_EXPRESSION_P2','AnalizadorLexico&SIntaxis.py',278),
  ('ARITHMETIC_EXPRESSION_P2 -> ARITHMETIC_EXPRESSION_P2 POWER_BY ARITHMETIC_EXPRESSION_P3','ARITHMETIC_EXPRESSION_P2',3,'p_ARITHMETIC_EXPRESSION_P2','AnalizadorLexico&SIntaxis.py',279),
  ('ARITHMETIC_EXPRESSION_P3 -> OPEN_PARENTHESIS ARITHMETIC_EXPRESSION CLOSE_PARENTHESIS','ARITHMETIC_EXPRESSION_P3',3,'p_ARITHMETIC_EXPRESSION_P3','AnalizadorLexico&SIntaxis.py',283),
  ('ARITHMETIC_EXPRESSION_P3 -> ANY_VALUE','ARITHMETIC_EXPRESSION_P3',1,'p_ARITHMETIC_EXPRESSION_P3','AnalizadorLexico&SIntaxis.py',284),
  ('LOGICAL_EXPRESSION -> LOGICAL_EXPRESSION_P1','LOGICAL_EXPRESSION',1,'p_LOGICAL_EXPRESSION','AnalizadorLexico&SIntaxis.py',290),
  ('LOGICAL_EXPRESSION -> LOGICAL_EXPRESSION OR LOGICAL_EXPRESSION_P1','LOGICAL_EXPRESSION',3,'p_LOGICAL_EXPRESSION','AnalizadorLexico&SIntaxis.py',291),
  ('LOGICAL_EXPRESSION_P1 -> LOGICAL_EXPRESSION_P2','LOGICAL_EXPRESSION_P1',1,'p_LOGICAL_EXPRESSION_P1','AnalizadorLexico&SIntaxis.py',295),
  ('LOGICAL_EXPRESSION_P1 -> LOGICAL_EXPRESSION_P1 AND LOGICAL_EXPRESSION_P2','LOGICAL_EXPRESSION_P1',3,'p_LOGICAL_EXPRESSION_P1','AnalizadorLexico&SIntaxis.py',296),
  ('LOGICAL_EXPRESSION_P2 -> LOGICAL_EXPRESSION_P3','LOGICAL_EXPRESSION_P2',1,'p_LOGICAL_EXPRESSION_P2','AnalizadorLexico&SIntaxis.py',300),
  ('LOGICAL_EXPRESSION_P2 -> NOT LOGICAL_EXPRESSION_P3','LOGICAL_EXPRESSION_P2',2,'p_LOGICAL_EXPRESSION_P2','AnalizadorLexico&SIntaxis.py',301),
  ('LOGICAL_EXPRESSION_P3 -> OPEN_PARENTHESIS LOGICAL_EXPRESSION CLOSE_PARENTHESIS','LOGICAL_EXPRESSION_P3',3,'p_LOGICAL_EXPRESSION_P3','AnalizadorLexico&SIntaxis.py',305),
  ('LOGICAL_EXPRESSION_P3 -> ARITHMETIC_EXPRESSION RELATIONAL_OPERATOR ARITHMETIC_EXPRESSION','LOGICAL_EXPRESSION_P3',3,'p_LOGICAL_EXPRESSION_P3','AnalizadorLexico&SIntaxis.py',306),
  ('RELATIONAL_OPERATOR -> EQUAL_TO','RELATIONAL_OPERATOR',1,'p_RELATIONAL_OPERATOR','AnalizadorLexico&SIntaxis.py',311),
  ('RELATIONAL_OPERATOR -> DIFFERENT_TO','RELATIONAL_OPERATOR',1,'p_RELATIONAL_OPERATOR','AnalizadorLexico&SIntaxis.py',312),
  ('RELATIONAL_OPERATOR -> LESS_THAN','RELATIONAL_OPERATOR',1,'p_RELATIONAL_OPERATOR','AnalizadorLexico&SIntaxis.py',313),
  ('RELATIONAL_OPERATOR -> GREATER_THAN','RELATIONAL_OPERATOR',1,'p_RELATIONAL_OPERATOR','AnalizadorLexico&SIntaxis.py',314),
  ('RELATIONAL_OPERATOR -> LESS_OR_EQUAL_THAN','RELATIONAL_OPERATOR',1,'p_RELATIONAL_OPERATOR','AnalizadorLexico&SIntaxis.py',315),
  ('RELATIONAL_OPERATOR -> GREATER_OR_EQUAL_THAN','RELATIONAL_OPERATOR',1,'p_RELATIONAL_OPERATOR','AnalizadorLexico&SIntaxis.py',316),
]
