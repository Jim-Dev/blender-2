import bpy


def create(obj):
    # generated by rigify.utils.write_metarig
    bpy.ops.object.mode_set(mode='EDIT')
    arm = obj.data

    for i in range(28):
        arm.rigify_layers.add()

    arm.rigify_layers[0].name = "head"
    arm.rigify_layers[0].row = 1
    arm.rigify_layers[1].name = " "
    arm.rigify_layers[1].row = 1
    arm.rigify_layers[2].name = "Spine"
    arm.rigify_layers[2].row = 2
    arm.rigify_layers[3].name = "Spine(Tweak)"
    arm.rigify_layers[3].row = 2
    arm.rigify_layers[4].name = "Tail"
    arm.rigify_layers[4].row = 3
    arm.rigify_layers[5].name = "Tail(Tweak)"
    arm.rigify_layers[5].row = 3
    arm.rigify_layers[6].name = "Leg.F.L (FK)"
    arm.rigify_layers[6].row = 4
    arm.rigify_layers[7].name = "Leg.F.L (IK)"
    arm.rigify_layers[7].row = 5
    arm.rigify_layers[8].name = "Leg.F.L (Tweak)"
    arm.rigify_layers[8].row = 6
    arm.rigify_layers[9].name = "Leg.F.R (FK)"
    arm.rigify_layers[9].row = 4
    arm.rigify_layers[10].name = "Leg.F.R (IK)"
    arm.rigify_layers[10].row = 5
    arm.rigify_layers[11].name = "Leg.F.R (Tweak)"
    arm.rigify_layers[11].row = 6
    arm.rigify_layers[12].name = "Leg.B.L (FK)"
    arm.rigify_layers[12].row = 7
    arm.rigify_layers[13].name = "Leg.B.L (IK)"
    arm.rigify_layers[13].row = 8
    arm.rigify_layers[14].name = "Leg.B.L (Tweak)"
    arm.rigify_layers[14].row = 9
    arm.rigify_layers[15].name = "Leg.B.R (FK)"
    arm.rigify_layers[15].row = 7
    arm.rigify_layers[16].name = "Leg.B.R (IK)"
    arm.rigify_layers[16].row = 8
    arm.rigify_layers[17].name = "Leg.B.R (Tweak)"
    arm.rigify_layers[17].row = 9
    arm.rigify_layers[18].name = " "
    arm.rigify_layers[18].row = 1
    arm.rigify_layers[19].name = " "
    arm.rigify_layers[19].row = 1
    arm.rigify_layers[20].name = " "
    arm.rigify_layers[20].row = 1
    arm.rigify_layers[21].name = " "
    arm.rigify_layers[21].row = 1
    arm.rigify_layers[22].name = " "
    arm.rigify_layers[22].row = 1
    arm.rigify_layers[23].name = " "
    arm.rigify_layers[23].row = 1
    arm.rigify_layers[24].name = " "
    arm.rigify_layers[24].row = 1
    arm.rigify_layers[25].name = " "
    arm.rigify_layers[25].row = 1
    arm.rigify_layers[26].name = " "
    arm.rigify_layers[26].row = 1
    arm.rigify_layers[27].name = " "
    arm.rigify_layers[27].row = 1

    bones = {}

    bone = arm.edit_bones.new('spine')
    bone.head[:] = 0.0000, 1.9143, 2.7813
    bone.tail[:] = 0.0000, 1.0299, 2.7618
    bone.roll = 0.0000
    bone.use_connect = False
    bones['spine'] = bone.name
    bone = arm.edit_bones.new('thigh.B.L')
    bone.head[:] = 0.5034, 1.9143, 2.7813
    bone.tail[:] = 0.5034, 1.8080, 1.3937
    bone.roll = 0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine']]
    bones['thigh.B.L'] = bone.name
    bone = arm.edit_bones.new('thigh.B.R')
    bone.head[:] = -0.5034, 1.9143, 2.7813
    bone.tail[:] = -0.5034, 1.8080, 1.3937
    bone.roll = -0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine']]
    bones['thigh.B.R'] = bone.name
    bone = arm.edit_bones.new('spine.001')
    bone.head[:] = 0.0000, 1.0299, 2.7618
    bone.tail[:] = -0.0000, -0.1236, 2.7221
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['spine']]
    bones['spine.001'] = bone.name
    bone = arm.edit_bones.new('Tail')
    bone.head[:] = 0.0000, 1.9143, 2.7813
    bone.tail[:] = 0.0000, 2.5888, 2.7813
    bone.roll = 0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine']]
    bones['Tail'] = bone.name
    bone = arm.edit_bones.new('shin.B.L')
    bone.head[:] = 0.5034, 1.8080, 1.3937
    bone.tail[:] = 0.5034, 1.9242, 0.6668
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['thigh.B.L']]
    bones['shin.B.L'] = bone.name
    bone = arm.edit_bones.new('shin.B.R')
    bone.head[:] = -0.5034, 1.8080, 1.3937
    bone.tail[:] = -0.5034, 1.9242, 0.6668
    bone.roll = -0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['thigh.B.R']]
    bones['shin.B.R'] = bone.name
    bone = arm.edit_bones.new('spine.002')
    bone.head[:] = -0.0000, -0.1236, 2.7221
    bone.tail[:] = 0.0000, -1.6591, 2.7404
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['spine.001']]
    bones['spine.002'] = bone.name
    bone = arm.edit_bones.new('Tail.001')
    bone.head[:] = 0.0000, 2.5888, 2.7813
    bone.tail[:] = 0.0000, 3.2635, 2.7813
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Tail']]
    bones['Tail.001'] = bone.name
    bone = arm.edit_bones.new('foot.B.L')
    bone.head[:] = 0.5034, 1.9242, 0.6668
    bone.tail[:] = 0.5034, 1.4276, 0.0000
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['shin.B.L']]
    bones['foot.B.L'] = bone.name
    bone = arm.edit_bones.new('heel.B.L')
    bone.head[:] = 0.5034, 1.9242, 0.6668
    bone.tail[:] = 0.5034, 2.1110, 0.0000
    bone.roll = 3.1416
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['shin.B.L']]
    bones['heel.B.L'] = bone.name
    bone = arm.edit_bones.new('foot.B.R')
    bone.head[:] = -0.5034, 1.9242, 0.6668
    bone.tail[:] = -0.5034, 1.4276, 0.0000
    bone.roll = -0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['shin.B.R']]
    bones['foot.B.R'] = bone.name
    bone = arm.edit_bones.new('heel.B.R')
    bone.head[:] = -0.5034, 1.9242, 0.6668
    bone.tail[:] = -0.5034, 2.1110, 0.0000
    bone.roll = -3.1416
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['shin.B.R']]
    bones['heel.B.R'] = bone.name
    bone = arm.edit_bones.new('spine.003')
    bone.head[:] = 0.0000, -1.6591, 2.7404
    bone.tail[:] = -0.0000, -2.9270, 2.8127
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['spine.002']]
    bones['spine.003'] = bone.name
    bone = arm.edit_bones.new('Tail.002')
    bone.head[:] = 0.0000, 3.2635, 2.7813
    bone.tail[:] = 0.0000, 3.9380, 2.7813
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Tail.001']]
    bones['Tail.002'] = bone.name
    bone = arm.edit_bones.new('toe.B.L')
    bone.head[:] = 0.5034, 1.4276, 0.0000
    bone.tail[:] = 0.5034, 1.2532, 0.0000
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['foot.B.L']]
    bones['toe.B.L'] = bone.name
    bone = arm.edit_bones.new('heel.02.B.L')
    bone.head[:] = 0.4049, 1.8822, 0.0000
    bone.tail[:] = 0.6124, 1.8822, 0.0000
    bone.roll = 0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['heel.B.L']]
    bones['heel.02.B.L'] = bone.name
    bone = arm.edit_bones.new('toe.B.R')
    bone.head[:] = -0.5034, 1.4276, 0.0000
    bone.tail[:] = -0.5034, 1.2532, 0.0000
    bone.roll = -0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['foot.B.R']]
    bones['toe.B.R'] = bone.name
    bone = arm.edit_bones.new('heel.B.R.02')
    bone.head[:] = -0.2653, 1.8822, 0.0000
    bone.tail[:] = -0.4728, 1.8822, 0.0000
    bone.roll = 0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['heel.B.R']]
    bones['heel.B.R.02'] = bone.name
    bone = arm.edit_bones.new('spine.004')
    bone.head[:] = -0.0000, -2.9270, 2.8127
    bone.tail[:] = -0.0000, -3.3999, 2.6305
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['spine.003']]
    bones['spine.004'] = bone.name
    bone = arm.edit_bones.new('shoulder.L')
    bone.head[:] = -0.0000, -2.1957, 2.7754
    bone.tail[:] = 0.6755, -2.1790, 2.8195
    bone.roll = -1.6365
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine.003']]
    bones['shoulder.L'] = bone.name
    bone = arm.edit_bones.new('shoulder.R')
    bone.head[:] = 0.0000, -2.1957, 2.7754
    bone.tail[:] = -0.6755, -2.1790, 2.8195
    bone.roll = 1.6365
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine.003']]
    bones['shoulder.R'] = bone.name
    bone = arm.edit_bones.new('Tail.003')
    bone.head[:] = 0.0000, 3.9380, 2.7813
    bone.tail[:] = 0.0000, 4.6019, 2.7813
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Tail.002']]
    bones['Tail.003'] = bone.name
    bone = arm.edit_bones.new('spine.005')
    bone.head[:] = -0.0000, -3.3999, 2.6305
    bone.tail[:] = -0.0000, -3.8736, 2.4490
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['spine.004']]
    bones['spine.005'] = bone.name
    bone = arm.edit_bones.new('thigh.F.L')
    bone.head[:] = 0.6755, -2.1790, 2.8195
    bone.tail[:] = 0.6755, -1.6893, 1.5380
    bone.roll = 0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['shoulder.L']]
    bones['thigh.F.L'] = bone.name
    bone = arm.edit_bones.new('thigh.F.R')
    bone.head[:] = -0.6755, -2.1790, 2.8195
    bone.tail[:] = -0.6755, -1.6893, 1.5380
    bone.roll = -0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['shoulder.R']]
    bones['thigh.F.R'] = bone.name
    bone = arm.edit_bones.new('spine.006')
    bone.head[:] = -0.0000, -3.8736, 2.4490
    bone.tail[:] = -0.0000, -5.2975, 1.7647
    bone.roll = -6.2832
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['spine.005']]
    bones['spine.006'] = bone.name
    bone = arm.edit_bones.new('shin.F.L')
    bone.head[:] = 0.6755, -1.6893, 1.5380
    bone.tail[:] = 0.6755, -1.7293, 0.4603
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['thigh.F.L']]
    bones['shin.F.L'] = bone.name
    bone = arm.edit_bones.new('shin.F.R')
    bone.head[:] = -0.6755, -1.6893, 1.5380
    bone.tail[:] = -0.6755, -1.7293, 0.4603
    bone.roll = -0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['thigh.F.R']]
    bones['shin.F.R'] = bone.name
    bone = arm.edit_bones.new('Jaw')
    bone.head[:] = -0.0000, -4.3479, 1.8376
    bone.tail[:] = -0.0000, -5.5175, 1.4433
    bone.roll = 0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine.006']]
    bones['Jaw'] = bone.name
    bone = arm.edit_bones.new('foot.F.L')
    bone.head[:] = 0.6755, -1.7293, 0.4603
    bone.tail[:] = 0.6755, -2.0911, 0.0000
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['shin.F.L']]
    bones['foot.F.L'] = bone.name
    bone = arm.edit_bones.new('heel.F.L')
    bone.head[:] = 0.6755, -1.7293, 0.4603
    bone.tail[:] = 0.6755, -1.4838, 0.0000
    bone.roll = 3.1416
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['shin.F.L']]
    bones['heel.F.L'] = bone.name
    bone = arm.edit_bones.new('foot.F.R')
    bone.head[:] = -0.6755, -1.7293, 0.4603
    bone.tail[:] = -0.6755, -2.0911, 0.0000
    bone.roll = -0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['shin.F.R']]
    bones['foot.F.R'] = bone.name
    bone = arm.edit_bones.new('heel.F.R')
    bone.head[:] = -0.6755, -1.7293, 0.4603
    bone.tail[:] = -0.6755, -1.4838, 0.0000
    bone.roll = -3.1416
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['shin.F.R']]
    bones['heel.F.R'] = bone.name
    bone = arm.edit_bones.new('toe.F.L')
    bone.head[:] = 0.6755, -2.0911, 0.0000
    bone.tail[:] = 0.6755, -2.2655, 0.0000
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['foot.F.L']]
    bones['toe.F.L'] = bone.name
    bone = arm.edit_bones.new('heel.F.L.02')
    bone.head[:] = 0.5769, -1.7126, 0.0000
    bone.tail[:] = 0.7845, -1.7126, 0.0000
    bone.roll = 0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['heel.F.L']]
    bones['heel.F.L.02'] = bone.name
    bone = arm.edit_bones.new('toe.F.R')
    bone.head[:] = -0.6755, -2.0911, 0.0000
    bone.tail[:] = -0.6755, -2.2655, 0.0000
    bone.roll = -0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['foot.F.R']]
    bones['toe.F.R'] = bone.name
    bone = arm.edit_bones.new('heel.F.R.02')
    bone.head[:] = -0.5769, -1.7126, 0.0000
    bone.tail[:] = -0.7845, -1.7126, 0.0000
    bone.roll = -0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['heel.F.R']]
    bones['heel.F.R.02'] = bone.name

    bpy.ops.object.mode_set(mode='OBJECT')
    pbone = obj.pose.bones[bones['spine']]
    pbone.rigify_type = 'pitchipoy.super_torso_turbo'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.chain_bone_controls = "1, 2, 3"
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.neck_pos = 5
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.tweak_layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['thigh.B.L']]
    pbone.rigify_type = 'biped.leg'
    pbone.lock_location = (True, True, True)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.separate_ik_layers = True
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.ik_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.separate_hose_layers = True
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.hose_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['thigh.B.R']]
    pbone.rigify_type = 'biped.leg'
    pbone.lock_location = (True, True, True)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.separate_ik_layers = True
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.ik_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.separate_hose_layers = True
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.hose_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['spine.001']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Tail']]
    pbone.rigify_type = 'pitchipoy.simple_tentacle'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.tweak_layers = [False, False, False, False, False, True, True, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['shin.B.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['shin.B.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['spine.002']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Tail.001']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['foot.B.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['heel.B.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['foot.B.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['heel.B.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['spine.003']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Tail.002']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['toe.B.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['heel.02.B.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['toe.B.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['heel.B.R.02']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['spine.004']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['shoulder.L']]
    pbone.rigify_type = 'basic.copy'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['shoulder.R']]
    pbone.rigify_type = 'basic.copy'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Tail.003']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['spine.005']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['thigh.F.L']]
    pbone.rigify_type = 'biped.leg'
    pbone.lock_location = (True, True, True)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.separate_ik_layers = True
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.ik_layers = [False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.separate_hose_layers = True
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.hose_layers = [False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['thigh.F.R']]
    pbone.rigify_type = 'biped.leg'
    pbone.lock_location = (True, True, True)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.separate_ik_layers = True
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.ik_layers = [False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.separate_hose_layers = True
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.hose_layers = [False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['spine.006']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['shin.F.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['shin.F.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Jaw']]
    pbone.rigify_type = 'basic.copy'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['foot.F.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['heel.F.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['foot.F.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['heel.F.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['toe.F.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['heel.F.L.02']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['toe.F.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['heel.F.R.02']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

    bpy.ops.object.mode_set(mode='EDIT')
    for bone in arm.edit_bones:
        bone.select = False
        bone.select_head = False
        bone.select_tail = False
    for b in bones:
        bone = arm.edit_bones[bones[b]]
        bone.select = True
        bone.select_head = True
        bone.select_tail = True
        arm.edit_bones.active = bone

    arm.layers = [(x in [0, 2, 4, 6, 7, 9, 10, 12, 15]) for x in range(32)]

if __name__ == "__main__":
    create(bpy.context.active_object)