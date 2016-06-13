
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '383441ADA42C02CE12D692FCE96C637D'
    
_lr_action_items = {'DIGITO':([0,4,7,8,9,13,19,39,40,41,43,47,48,],[4,10,-14,4,4,-9,4,43,43,43,46,48,49,]),'ESPACIO':([5,12,17,18,20,24,25,27,28,29,30,31,35,36,42,44,45,49,],[13,13,-18,-7,13,13,13,13,13,-16,13,13,-12,-10,-5,-6,-4,-17,]),'NUM':([13,26,33,],[-9,35,35,]),'ANNO':([7,21,22,23,],[-14,29,29,29,]),'TIMEZONE':([11,13,19,],[17,-9,17,]),'$end':([2,17,18,20,25,27,32,34,35,36,37,],[0,-18,-7,-11,-13,-11,-3,-1,-12,-10,-2,]),'SEPARADOR':([1,3,6,10,14,15,16,],[7,7,-15,-8,7,7,7,]),'HORA':([46,],[47,]),'FORMATO':([13,26,38,],[-9,36,36,]),'MES':([0,7,8,13,19,],[6,-14,6,-9,6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'F':([20,27,],[25,37,]),'E':([5,12,20,24,25,27,28,30,31,],[11,19,26,11,33,38,39,40,41,]),'D':([0,8,9,19,],[1,14,16,1,]),'K':([20,25,],[27,34,]),'S':([0,],[2,]),'H':([39,40,41,],[42,44,45,]),'M':([0,8,19,],[3,15,3,]),'C':([1,3,14,15,16,],[8,9,21,22,23,]),'A':([21,22,23,],[28,30,31,]),'X':([5,12,24,],[12,20,32,]),'T':([11,19,],[18,18,]),'P':([0,19,],[5,24,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> S","S'",1,None,None,None),
  ('S -> P X X F K','S',5,'p_fecha_conversion','proyecto.py',77),
  ('S -> P X X K F','S',5,'p_fecha_conversion','proyecto.py',78),
  ('S -> P X E P X','S',5,'p_fecha_conversion','proyecto.py',79),
  ('P -> M C D C A E H','P',7,'p_fecha_hora','proyecto.py',83),
  ('P -> D C D C A E H','P',7,'p_fecha_hora','proyecto.py',84),
  ('P -> D C M C A E H','P',7,'p_fecha_hora','proyecto.py',85),
  ('X -> E T','X',2,'p_espacio_timezone','proyecto.py',116),
  ('D -> DIGITO DIGITO','D',2,'p_doble_digito','proyecto.py',122),
  ('E -> ESPACIO','E',1,'p_espacio','proyecto.py',128),
  ('F -> E FORMATO','F',2,'p_formato','proyecto.py',134),
  ('F -> <empty>','F',0,'p_formato','proyecto.py',135),
  ('K -> E NUM','K',2,'p_anadir_dias','proyecto.py',142),
  ('K -> <empty>','K',0,'p_anadir_dias','proyecto.py',143),
  ('C -> SEPARADOR','C',1,'p_separador','proyecto.py',150),
  ('M -> MES','M',1,'p_mes','proyecto.py',156),
  ('A -> ANNO','A',1,'p_anno','proyecto.py',162),
  ('H -> DIGITO DIGITO HORA DIGITO DIGITO','H',5,'p_hora','proyecto.py',168),
  ('T -> TIMEZONE','T',1,'p_timezone','proyecto.py',184),
]
