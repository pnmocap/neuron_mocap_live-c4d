import c4d
from neuron_defs import *
import neuron_connection
import neuron_recorder

class NeuronTagData(c4d.plugins.TagData):
   def Init(self, node):
      node.GetDataInstance().SetBool(ID_TAG_CHARACTER_JOINTS + 1, True)
      node.GetDataInstance().SetBool(ID_TAG_CHARACTER_JOINTS + 2, True)

      for i in range(1, len(NEURON_JOINTS)) :
         node.GetDataInstance().SetBool(ID_TAG_CHARACTER_JOINTS + 3*i + 1, True)
         node.GetDataInstance().SetBool(ID_TAG_CHARACTER_JOINTS + 3*i + 2, False)

      return True

   def GetDDescription(self, node, description, flags):
      singleID = description.GetSingleDescID()
      if not description.LoadDescription(node.GetType()):
         return False
      singleID = description.GetSingleDescID()

      desc_id = c4d.DescID(c4d.DescLevel(ID_TAG_CHARACTER_GROUP, c4d.DTYPE_GROUP, node.GetType()))
      if singleID is None or desc_id.IsPartOf(singleID):
         bc = c4d.GetCustomDataTypeDefault(c4d.DTYPE_GROUP)
         bc.SetInt32(c4d.DESC_COLUMNS, 3)
         bc.SetString(c4d.DESC_NAME, "Character")
         bc.SetBool(c4d.DESC_DEFAULT, True)
         description.SetParameter(desc_id, bc, c4d.ID_TAGPROPERTIES)

      desc_id = c4d.DescID(c4d.DescLevel(ID_TAG_CHARACTER_NAME, c4d.DTYPE_STRING, node.GetType()))
      if singleID is None or desc_id.IsPartOf(singleID):
         bc = c4d.GetCustomDataTypeDefault(c4d.DTYPE_STRING)
         bc.SetString(c4d.DESC_NAME, "Name")
         bc.SetString(c4d.DESC_SHORT_NAME, "Name")
         bc.SetInt32(c4d.DESC_ANIMATE, c4d.DESC_ANIMATE_OFF)
         bc.SetBool(c4d.DESC_SCALEH, True)
         description.SetParameter(desc_id, bc, ID_TAG_CHARACTER_GROUP)

      desc_id = c4d.DescID(c4d.DescLevel(ID_TAG_JOINTS_CONTROL_GROUP, c4d.DTYPE_GROUP, node.GetType()))
      if singleID is None or desc_id.IsPartOf(singleID):
         bc = c4d.GetCustomDataTypeDefault(c4d.DTYPE_GROUP)
         bc.SetInt32(c4d.DESC_COLUMNS, 2)
         bc.SetString(c4d.DESC_NAME, "Joints Control")
         bc.SetBool(c4d.DESC_DEFAULT, True)
         description.SetParameter(desc_id, bc, c4d.ID_TAGPROPERTIES)

      desc_id = c4d.DescID(c4d.DescLevel(ID_TAG_DETECT_JOINTS, c4d.DTYPE_BUTTON, node.GetType()))
      if singleID is None or desc_id.IsPartOf(singleID):
         bc = c4d.GetCustomDataTypeDefault(c4d.DTYPE_BUTTON)
         bc.SetString(c4d.DESC_NAME, "Detect Joints Map")
         bc.SetString(c4d.DESC_SHORT_NAME, "Detect Joints Map")
         bc.SetInt32(c4d.DESC_ANIMATE, c4d.DESC_ANIMATE_OFF)
         bc.SetInt32(c4d.DESC_CUSTOMGUI, c4d.CUSTOMGUI_BUTTON)
         bc.SetBool(c4d.DESC_SCALEH, True)
         description.SetParameter(desc_id, bc, ID_TAG_JOINTS_CONTROL_GROUP)

      desc_id = c4d.DescID(c4d.DescLevel(ID_TAG_CLEAR_JOINTS, c4d.DTYPE_BUTTON, node.GetType()))
      if singleID is None or desc_id.IsPartOf(singleID):
         bc = c4d.GetCustomDataTypeDefault(c4d.DTYPE_BUTTON)
         bc.SetString(c4d.DESC_NAME, "Clear Joints Map")
         bc.SetString(c4d.DESC_SHORT_NAME, "Clear Joints Map")
         bc.SetInt32(c4d.DESC_ANIMATE, c4d.DESC_ANIMATE_OFF)
         bc.SetInt32(c4d.DESC_CUSTOMGUI, c4d.CUSTOMGUI_BUTTON)
         bc.SetBool(c4d.DESC_SCALEH, True)
         description.SetParameter(desc_id, bc, ID_TAG_JOINTS_CONTROL_GROUP)

      desc_id = c4d.DescID(c4d.DescLevel(ID_TAG_SET_T_POSE, c4d.DTYPE_BUTTON, node.GetType()))
      if singleID is None or desc_id.IsPartOf(singleID):
         bc = c4d.GetCustomDataTypeDefault(c4d.DTYPE_BUTTON)
         bc.SetString(c4d.DESC_NAME, "Set T-Pose")
         bc.SetString(c4d.DESC_SHORT_NAME, "Set T-Pose")
         bc.SetInt32(c4d.DESC_ANIMATE, c4d.DESC_ANIMATE_OFF)
         bc.SetInt32(c4d.DESC_CUSTOMGUI, c4d.CUSTOMGUI_BUTTON)
         description.SetParameter(desc_id, bc, ID_TAG_JOINTS_CONTROL_GROUP)

      desc_id = c4d.DescID(c4d.DescLevel(ID_TAG_GOTO_T_POSE, c4d.DTYPE_BUTTON, node.GetType()))
      if singleID is None or desc_id.IsPartOf(singleID):
         bc = c4d.GetCustomDataTypeDefault(c4d.DTYPE_BUTTON)
         bc.SetString(c4d.DESC_NAME, "Go to T-Pose")
         bc.SetString(c4d.DESC_SHORT_NAME, "Go to T-Pose")
         bc.SetInt32(c4d.DESC_ANIMATE, c4d.DESC_ANIMATE_OFF)
         bc.SetInt32(c4d.DESC_CUSTOMGUI, c4d.CUSTOMGUI_BUTTON)
         description.SetParameter(desc_id, bc, ID_TAG_JOINTS_CONTROL_GROUP)

      desc_id = c4d.DescID(c4d.DescLevel(ID_TAG_SCALE_ROOT_POSITION, c4d.DTYPE_BOOL, node.GetType()))
      if singleID is None or desc_id.IsPartOf(singleID):
         bc = c4d.GetCustomDataTypeDefault(c4d.DTYPE_BOOL)
         bc.SetString(c4d.DESC_NAME, "Scale Root Position")
         bc.SetString(c4d.DESC_SHORT_NAME, "Scale Root Position")
         bc.SetInt32(c4d.DESC_ANIMATE, c4d.DESC_ANIMATE_OFF)
         bc.SetBool(c4d.DESC_SCALEH, True)
         description.SetParameter(desc_id, bc, ID_TAG_JOINTS_CONTROL_GROUP)

      desc_id = c4d.DescID(c4d.DescLevel(ID_TAG_JOINTS_GROUP, c4d.DTYPE_GROUP, node.GetType()))
      if singleID is None or desc_id.IsPartOf(singleID):
         bc = c4d.GetCustomDataTypeDefault(c4d.DTYPE_GROUP)
         bc.SetInt32(c4d.DESC_COLUMNS, 3)
         bc.SetString(c4d.DESC_NAME, "Joints Map")
         bc.SetBool(c4d.DESC_DEFAULT, True)
         description.SetParameter(desc_id, bc, c4d.ID_TAGPROPERTIES)

      for idx in range(len(NEURON_JOINTS)):
         mg = node.GetDataInstance().GetData(ID_TAG_T_POSE_MATRIX + idx*3)

         joint = NEURON_JOINTS[idx]
         desc_id = c4d.DescID(c4d.DescLevel(ID_TAG_CHARACTER_JOINTS + idx*3, c4d.DTYPE_BASELISTLINK, node.GetType()))
         if singleID is None or desc_id.IsPartOf(singleID):
            bc = c4d.GetCustomDataTypeDefault(c4d.DTYPE_BASELISTLINK)
            if mg:
               bc.SetString(c4d.DESC_NAME, "{0} T".format(joint))
               bc.SetString(c4d.DESC_SHORT_NAME, "{0} T".format(joint))
            else:
               bc.SetString(c4d.DESC_NAME, joint)
               bc.SetString(c4d.DESC_SHORT_NAME, joint)
            bc.SetInt32(c4d.DESC_ANIMATE, c4d.DESC_ANIMATE_OFF)
            bc.SetBool(c4d.DESC_FORBID_INLINE_FOLDING, True)
            description.SetParameter(desc_id, bc, ID_TAG_JOINTS_GROUP)

         desc_id = c4d.DescID(c4d.DescLevel(ID_TAG_CHARACTER_JOINTS + idx*3 + 1, c4d.DTYPE_BOOL, node.GetType()))
         if singleID is None or desc_id.IsPartOf(singleID):
            bc = c4d.GetCustomDataTypeDefault(c4d.DTYPE_BOOL)
            bc.SetString(c4d.DESC_NAME, "R")
            bc.SetString(c4d.DESC_SHORT_NAME, "R")
            bc.SetInt32(c4d.DESC_ANIMATE, c4d.DESC_ANIMATE_OFF)
            bc.SetBool(c4d.DESC_DEFAULT, True)
            description.SetParameter(desc_id, bc, ID_TAG_JOINTS_GROUP)

         desc_id = c4d.DescID(c4d.DescLevel(ID_TAG_CHARACTER_JOINTS + idx*3 + 2, c4d.DTYPE_BOOL, node.GetType()))
         if singleID is None or desc_id.IsPartOf(singleID):
            bc = c4d.GetCustomDataTypeDefault(c4d.DTYPE_BOOL)
            bc.SetString(c4d.DESC_NAME, "P")
            bc.SetString(c4d.DESC_SHORT_NAME, "P")
            bc.SetInt32(c4d.DESC_ANIMATE, c4d.DESC_ANIMATE_OFF)
            description.SetParameter(desc_id, bc, ID_TAG_JOINTS_GROUP)

         desc_id = c4d.DescID(c4d.DescLevel(ID_TAG_CHARACTER_JOINTS_NAME + idx, c4d.DTYPE_STRING, node.GetType()))
         if singleID is None or desc_id.IsPartOf(singleID):
            bc = c4d.GetCustomDataTypeDefault(c4d.DTYPE_STRING)
            bc.SetInt32(c4d.DESC_ANIMATE, c4d.DESC_ANIMATE_OFF)
            bc.SetBool(c4d.DESC_HIDE, True)
            description.SetParameter(desc_id, bc, ID_TAG_JOINTS_GROUP)

         desc_id = c4d.DescID(c4d.DescLevel(ID_TAG_T_POSE_MATRIX + idx*3, c4d.DTYPE_MATRIX, node.GetType()))
         if singleID is None or desc_id.IsPartOf(singleID):
            bc = c4d.GetCustomDataTypeDefault(c4d.DTYPE_MATRIX)
            bc.SetInt32(c4d.DESC_ANIMATE, c4d.DESC_ANIMATE_OFF)
            bc.SetBool(c4d.DESC_HIDE, True)
            description.SetParameter(desc_id, bc, ID_TAG_JOINTS_GROUP)

         desc_id = c4d.DescID(c4d.DescLevel(ID_TAG_T_POSE_MATRIX + idx*3 + 1, c4d.DTYPE_MATRIX, node.GetType()))
         if singleID is None or desc_id.IsPartOf(singleID):
            bc = c4d.GetCustomDataTypeDefault(c4d.DTYPE_MATRIX)
            bc.SetInt32(c4d.DESC_ANIMATE, c4d.DESC_ANIMATE_OFF)
            bc.SetBool(c4d.DESC_HIDE, True)
            description.SetParameter(desc_id, bc, ID_TAG_JOINTS_GROUP)

         desc_id = c4d.DescID(c4d.DescLevel(ID_TAG_T_POSE_MATRIX + idx*3 + 2, c4d.DTYPE_MATRIX, node.GetType()))
         if singleID is None or desc_id.IsPartOf(singleID):
            bc = c4d.GetCustomDataTypeDefault(c4d.DTYPE_MATRIX)
            bc.SetInt32(c4d.DESC_ANIMATE, c4d.DESC_ANIMATE_OFF)
            bc.SetBool(c4d.DESC_HIDE, True)
            description.SetParameter(desc_id, bc, ID_TAG_JOINTS_GROUP)

      return True, flags | c4d.DESCFLAGS_DESC_LOADED

   def __searchHierarchy(self, obj, name):
      if obj is None:
         return None

      if obj.GetName() == name:
         return obj

      for child in obj.GetChildren():
         result = self.__searchHierarchy(child, name)
         if result is not None:
            return result
      return None

   def GetDParameter(self, node, id, flags):
      id = id[0].id
      if id == ID_TAG_CHARACTER_NAME:
         return True, node.GetDataInstance().GetString(ID_TAG_CHARACTER_NAME), c4d.DESCFLAGS_GET_PARAM_GET

      if id == ID_TAG_SCALE_ROOT_POSITION:
         return True, node.GetDataInstance().GetBool(ID_TAG_SCALE_ROOT_POSITION), c4d.DESCFLAGS_GET_PARAM_GET

      for idx in range(len(NEURON_JOINTS)):
         if id == ID_TAG_CHARACTER_JOINTS + idx*3:
            joint = node.GetDataInstance().GetData(id)
            if joint is None:
               joint_name = node.GetDataInstance().GetData(ID_TAG_CHARACTER_JOINTS_NAME + idx)
               if joint_name is not None and node.GetObject() is not None:
                  joint = self.__searchHierarchy(node.GetObject(), joint_name)
                  if joint is not None:
                     node.GetDataInstance().SetData(id, joint)
            return True, joint, c4d.DESCFLAGS_GET_PARAM_GET

         if id == ID_TAG_CHARACTER_JOINTS + idx*3 + 1:
            return True, node.GetDataInstance().GetBool(id), c4d.DESCFLAGS_GET_PARAM_GET

         if id == ID_TAG_CHARACTER_JOINTS + idx*3 + 2:
            return True, node.GetDataInstance().GetBool(id), c4d.DESCFLAGS_GET_PARAM_GET

         if id == ID_TAG_CHARACTER_JOINTS_NAME + idx:
            joint_name = node.GetDataInstance().GetData(id)
            return True, joint_name, c4d.DESCFLAGS_GET_PARAM_GET

         if id == ID_TAG_T_POSE_MATRIX + idx*3:
            return True, node.GetDataInstance().GetData(id), c4d.DESCFLAGS_GET_PARAM_GET

         if id == ID_TAG_T_POSE_MATRIX + idx*3 + 1:
            return True, node.GetDataInstance().GetData(id), c4d.DESCFLAGS_GET_PARAM_GET

         if id == ID_TAG_T_POSE_MATRIX + idx*3 + 2:
            return True, node.GetDataInstance().GetData(id), c4d.DESCFLAGS_GET_PARAM_GET

      return False

   def SetDParameter(self, node, id, t_data, flags):
      id = id[0].id

      if id == ID_TAG_CHARACTER_NAME:
         node.GetDataInstance().SetString(ID_TAG_CHARACTER_NAME, t_data)
         return True, flags | c4d.DESCFLAGS_SET_PARAM_SET

      if id == ID_TAG_SCALE_ROOT_POSITION:
         node.GetDataInstance().SetBool(ID_TAG_SCALE_ROOT_POSITION, t_data)
         return True, flags | c4d.DESCFLAGS_SET_PARAM_SET

      for idx in range(len(NEURON_JOINTS)):
         if id == ID_TAG_CHARACTER_JOINTS + idx:
            node.GetDataInstance().SetData(id, t_data)
            node.GetDataInstance().RemoveData(ID_TAG_T_POSE_MATRIX + idx*3)
            node.GetDataInstance().RemoveData(ID_TAG_T_POSE_MATRIX + idx*3 + 1)
            node.GetDataInstance().RemoveData(ID_TAG_T_POSE_MATRIX + idx*3 + 2)
            if t_data is not None:
               node.GetDataInstance().SetData(ID_TAG_CHARACTER_JOINTS_NAME + idx, t_data.GetName())
            else:
               node.GetDataInstance().RemoveData(ID_TAG_CHARACTER_JOINTS_NAME + idx)
            return True, flags | c4d.DESCFLAGS_SET_PARAM_SET

         if id == ID_TAG_CHARACTER_JOINTS + idx*3 + 1:
            node.GetDataInstance().SetBool(id, t_data)
            return True, flags | c4d.DESCFLAGS_SET_PARAM_SET

         if id == ID_TAG_CHARACTER_JOINTS + idx*3 + 2:
            node.GetDataInstance().SetBool(id, t_data)
            return True, flags | c4d.DESCFLAGS_SET_PARAM_SET

         if id == ID_TAG_CHARACTER_JOINTS_NAME + idx:
            node.GetDataInstance().SetData(id, t_data)
            if t_data is not None:
               joint = self.__searchHierarchy(node.GetObject(), t_data)
               if joint is not None:
                  node.GetDataInstance().SetData(ID_TAG_CHARACTER_JOINTS + idx*3, joint)
            return True, flags | c4d.DESCFLAGS_SET_PARAM_SET

         if id == ID_TAG_T_POSE_MATRIX + idx*3:
            node.GetDataInstance().SetData(id, t_data)
            return True, flags | c4d.DESCFLAGS_SET_PARAM_SET

         if id == ID_TAG_T_POSE_MATRIX + idx*3 + 1:
            node.GetDataInstance().SetData(id, t_data)
            return True, flags | c4d.DESCFLAGS_SET_PARAM_SET

         if id == ID_TAG_T_POSE_MATRIX + idx*3 + 2:
            node.GetDataInstance().SetData(id, t_data)
            return True, flags | c4d.DESCFLAGS_SET_PARAM_SET

      return False

   def _setTPose(self, node):
      for i in range(len(NEURON_JOINTS)):
         target_joint = node.GetDataInstance().GetData(ID_TAG_CHARACTER_JOINTS + i*3)
         if target_joint is not None:
            node.GetDataInstance().SetMatrix(ID_TAG_T_POSE_MATRIX + i*3, target_joint.GetMg())
            node.GetDataInstance().SetMatrix(ID_TAG_T_POSE_MATRIX + i*3 + 1, target_joint.GetUpMg())
            node.GetDataInstance().SetMatrix(ID_TAG_T_POSE_MATRIX + i*3 + 2, target_joint.GetMl())

   def _gotoTPose(self, node):
      for i in range(len(NEURON_JOINTS)):
         target_joint = node.GetDataInstance().GetData(ID_TAG_CHARACTER_JOINTS + i*3)
         mg = node.GetDataInstance().GetData(ID_TAG_T_POSE_MATRIX + i*3)
         if target_joint is not None and mg is not None:
            target_joint.SetMg(mg)

   def __detectJointsMap(self, node, obj):
      if type(obj) is c4d.modules.character.CAJointObject:
         obj_name = obj.GetName()

         for idx in range(len(NEURON_JOINTS)):
            if obj_name.endswith(NEURON_JOINTS[idx]):
               node.GetDataInstance().SetData(ID_TAG_CHARACTER_JOINTS + idx*3, obj)
               node.GetDataInstance().SetData(ID_TAG_CHARACTER_JOINTS_NAME + idx, obj.GetName())
               break

      for child in obj.GetChildren():
         self.__detectJointsMap(node, child)

   def _detectJointsMap(self, node):
      self._clearJointsMap(node)
      obj = node.GetObject()
      if obj is not None:
         self.__detectJointsMap(node, obj)

   def _clearJointsMap(self, node):
      for idx in range(len(NEURON_JOINTS)):
         node.GetDataInstance().RemoveData(ID_TAG_CHARACTER_JOINTS + idx*3)
         node.GetDataInstance().RemoveData(ID_TAG_T_POSE_MATRIX + idx*3)
         node.GetDataInstance().RemoveData(ID_TAG_T_POSE_MATRIX + idx*3 + 1)
         node.GetDataInstance().RemoveData(ID_TAG_T_POSE_MATRIX + idx*3 + 2)
         node.GetDataInstance().RemoveData(ID_TAG_CHARACTER_JOINTS_NAME + idx)

   def Message(self, node, type, data):
      if type==c4d.MSG_DESCRIPTION_COMMAND:
         id = data['id'][0].id
         if id == ID_TAG_SET_T_POSE:
            self._setTPose(node)
            return True
         if id == ID_TAG_GOTO_T_POSE:
            self._gotoTPose(node)
            return True
         if id == ID_TAG_DETECT_JOINTS:
            self._detectJointsMap(node)
            return True
         if id == ID_TAG_CLEAR_JOINTS:
            self._clearJointsMap(node)
            return True
      return True

   def __getRootScaleFactor(self, tag, avatar):
      leg_pos = avatar.get_joint_by_name("RightLeg").get_local_position()
      if leg_pos is None:
         return None

      foot_pos = avatar.get_joint_by_name("RightFoot").get_local_position()
      if foot_pos is None:
         return None

      src_height = (c4d.Vector(leg_pos[0], leg_pos[1], leg_pos[2]) + 
         c4d.Vector(foot_pos[0], foot_pos[1], foot_pos[2])).GetLength()

      leg_mg = tag.GetDataInstance().GetData(ID_TAG_T_POSE_MATRIX + 3)
      if leg_mg is None:
         return None

      foot_mg = tag.GetDataInstance().GetData(ID_TAG_T_POSE_MATRIX + 9)
      if foot_mg is None:
         return None
      
      target_height = abs((foot_mg.off - leg_mg.off)[1])

      return target_height / src_height

   def __animateJoints(self, tag, avatar):
      hip_scale = 1
      if tag.GetDataInstance().GetBool(ID_TAG_SCALE_ROOT_POSITION):
         scale_factor = self.__getRootScaleFactor(tag, avatar)
         if scale_factor is not None:
            hip_scale = scale_factor

      for i in range(len(NEURON_JOINTS)):
         joint_name = NEURON_JOINTS[i]
         joint = avatar.get_joint_by_name(joint_name)
         if joint is None:
            continue

         ry, rx, rz = joint.get_local_rotation_by_euler()
         src_ml = c4d.utils.MatrixRotY(c4d.utils.Rad(ry)) * c4d.utils.MatrixRotX(c4d.utils.Rad(rx)) * c4d.utils.MatrixRotZ(c4d.utils.Rad(-rz))

         i = NEURON_JOINTS_INDEX_MAP[joint_name]
         target_joint = tag.GetDataInstance().GetData(ID_TAG_CHARACTER_JOINTS + i*3)
         r_enable = tag.GetDataInstance().GetBool(ID_TAG_CHARACTER_JOINTS + i*3 + 1)
         p_enable = tag.GetDataInstance().GetBool(ID_TAG_CHARACTER_JOINTS + i*3 + 2)
         target_mg = tag.GetDataInstance().GetData(ID_TAG_T_POSE_MATRIX + i*3)
         target_up_mg = tag.GetDataInstance().GetData(ID_TAG_T_POSE_MATRIX + i*3 + 1)
         target_ml = tag.GetDataInstance().GetData(ID_TAG_T_POSE_MATRIX + i*3 + 2)

         if target_joint is not None and target_mg is not None:
            if target_up_mg is None:
               target_up_mg = c4d.Matrix()

            if target_ml is None:
               target_ml = c4d.Matrix(target_mg)

            if r_enable:
               ml = target_ml * (~target_mg) * src_ml * target_mg
               target_joint.SetAbsRot(c4d.utils.MatrixToHPB(ml, target_joint.GetRotationOrder()))
            if p_enable:
               target_mg.off = c4d.Vector(0, 0, 0)
               p = joint.get_local_position()
               if p is not None:
                  target_up_mg.off = c4d.Vector(0, 0, 0)
                  src_pl = (~target_up_mg) * c4d.Vector(p[0], p[1], p[2])
                  src_pl[2] = -src_pl[2]
                  if joint_name == "Hips":
                     src_pl *= hip_scale
                  target_joint.SetAbsPos(src_pl)
               else:
                  target_joint.SetAbsPos(target_ml.off)

   def __recordKey(self, tag, t):
      for joint_index in range(len(NEURON_JOINTS)):
         target_joint = tag.GetDataInstance().GetData(ID_TAG_CHARACTER_JOINTS + joint_index*3)
         if target_joint is None:
            continue
         id_px = c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_REL_POSITION, c4d.DTYPE_VECTOR, 0), c4d.DescLevel(c4d.VECTOR_X, c4d.DTYPE_REAL, 0))
         id_py = c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_REL_POSITION, c4d.DTYPE_VECTOR, 0), c4d.DescLevel(c4d.VECTOR_Y, c4d.DTYPE_REAL, 0))
         id_pz = c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_REL_POSITION, c4d.DTYPE_VECTOR, 0), c4d.DescLevel(c4d.VECTOR_Z, c4d.DTYPE_REAL, 0))
         id_rx = c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_REL_ROTATION, c4d.DTYPE_VECTOR, 0), c4d.DescLevel(c4d.VECTOR_X, c4d.DTYPE_REAL, 0))
         id_ry = c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_REL_ROTATION, c4d.DTYPE_VECTOR, 0), c4d.DescLevel(c4d.VECTOR_Y, c4d.DTYPE_REAL, 0))
         id_rz = c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_REL_ROTATION, c4d.DTYPE_VECTOR, 0), c4d.DescLevel(c4d.VECTOR_Z, c4d.DTYPE_REAL, 0))
         pos = target_joint.GetRelPos()
         rot = target_joint.GetRelRot()
         id_list = [id_px, id_py, id_pz, id_rx, id_ry, id_rz]
         value_list = [pos[0], pos[1], pos[2], rot[0], rot[1], rot[2]]
         for value_index in range(6):
            id = id_list[value_index]
            value = value_list[value_index]
            tr = target_joint.FindCTrack(id)
            if tr is None:
               tr = c4d.CTrack(target_joint, id)
               target_joint.InsertTrackSorted(tr)
            curve = tr.GetCurve()
            key = curve.AddKey(t)
            key['key'].SetValue(curve, value)
            key['key'].SetInterpolation(curve, c4d.CINTERPOLATION_STEP)

   def Execute(self, tag, doc, op, bt, priority, flags):
      if neuron_connection.IsConnecting():
         chr_name = tag.GetDataInstance().GetString(ID_TAG_CHARACTER_NAME)
         avatar = neuron_connection.GetAvatar(chr_name)
         if avatar is not None:
            self.__animateJoints(tag, avatar)
            if neuron_recorder.IsRecording():
               self.__recordKey(tag, neuron_recorder.GetKeyTime())
      return c4d.EXECUTIONRESULT_OK
