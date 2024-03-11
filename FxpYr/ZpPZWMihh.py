expLinksDic = {}
expPropDic = {}
nodosDic = {}
def ItLRTKgmf(node, enum: str = "") -> str:
    try:
        vectColor = node.default_value
    except:
        vectColor = node
    if 'Vector' in str(type(vectColor)):
        return f"({vectColor[0]}, {vectColor[1]}, {vectColor[2]})"
    if node.bl_idname == "NodeSocketColor":
        return f"({vectColor[0]}, {vectColor[1]}, {vectColor[2]}, {vectColor[3]})"
    elif "Vector" in node.bl_idname:
        return f"({vectColor[0]}, {vectColor[1]}, {vectColor[2]})"
    elif node.bl_idname == "NodeSocketRotation":
        return f"({vectColor[0]}, {vectColor[1]}, {vectColor[2]})"
    elif node.bl_idname == "NodeSocketFloat":
        return f"\'{enum}\'"
def ODMuAEIrd(vect):
    return f"({vect[0]}, {vect[1]}, {vect[2]}, {vect[3]})"
def vAfqSCzgy(n, nodes):
    for n in nodes:
        if n.type == "TEX_IMAGE":
            export_TEX_IMAGE(n)
        if n.type == "TEX_COORD":
            export_TEX_COORD(n)
        if n.type == "MAPPING":
            cZwbFFCqj(n)
        if n.type == "BSDF_PRINCIPLED":
            gStRTgEJs(n)
        if n.type == "OUTPUT_MATERIAL":
            eIFRbtmOs(n)
        if n.type == "TEX_NOISE":
            EphkWZNUR(n)
        if n.type == "TEX_GRADIENT":
            MwMVeYvPY(n)
        if n.type == "VALTORGB":
            IwRYgpJRU(n)
        if n.type == "BSDF_GLOSSY":
            KDwwooecF(n)
        if n.type == "LAYER_WEIGHT":
            QfVExZeiT(n)
        if n.type == "FRESNEL":
            KynjtDIPu(n)
        if n.type == "EMISSION":
            XVrSIuNrv(n)
        if n.type == "BSDF_DIFFUSE":
            KjWhAwphM(n)
        if n.type == "MIX_SHADER":
            EaQoswpZO(n)
        if n.type == "BUMP":
            OkmOAFOEn(n)
        if n.type == "GAMMA":
            JrinVafsq(n)
        if n.type == "TEX_CHECKER":
            iWCoXXQkW(n)
        if n.type == "MIX":
            bylTZogcQ(n)
        if n.type == "RGBTOBW":
            CxbBrQiBS(n)
        if n.type == "TEX_MUSGRAVE":
            qrZytqUAJ(n)
        if n.type == "MATH":
            zLLbwwbNS(n)
        if n.type == "TEX_VORONOI":
            lJCKAlCBk(n)
        if n.type == "DISPLACEMENT":    
            yHnMJiCSfMENT(n)
        if n.type == "BLACKBODY":   
            kohGcxBEM(n)
        if n.type == "BRIGHTCONTRAST":   
            gVyHoIRcK(n)
        if n.type == "BACKGROUND":   
            MFZepBrBY(n)
        if n.type == "AMBIENT_OCCLUSION":   
            GqeWkiGhY(n)
        if n.type == "BSDF_GLASS":   
            RZrDnQyCc(n)
        if n.type == "BSDF_HAIR":   
            xZFNmztIz(n)
        if n.type == "BSDF_HAIR_PRINCIPLED":
            xZFNmztIz_PRINCIPLED(n)
        if n.type == "BEVEL":
            NoMQYIWaf(n)
        if n.type == "ATTRIBUTE":
            zZTVDXLkl(n)
        if n.type == "BSDF_REFRACTION":
            LGHJGbWdT(n)
        if n.type == "BSDF_SHEEN":
            NBjqHyQqA(n)
        if n.type == "BSDF_TOON":
            pBBcThEHJ(n)
        if n.type == "BSDF_TRANSLUCENT":
            aCMpWANas(n)
        if n.type == "BSDF_TRANSPARENT":
            ToQBHwBWT(n)
        if n.type == "EEVEE_SPECULAR":            
            RUnAudCpr(n)
        if n.type == "COMBRGB":
            rCCnTnNbv(n)
        if n.type == "COMBHSV":
            eFYwbMveu(n)
        if n.type == "COMBXYZ":
            bqfCDkyQx(n)
        if n.type == "CLAMP":
            wfWwqrVlc(n)
        if n.type == "COMBINE_COLOR":
            jQXBHkVtI(n)
        if n.type == "CURVE_FLOAT":
            kerYxfLer(n)
        if n.type == "HUE_SAT":
            yovKHNxZd(n)
        if n.type == "INVERT":
            nPnoFLiwy(n)
        if n.type == "LIGHT_FALLOFF":
            LlzxgAPQg(n)
        if n.type == "MAP_RANGE":
            mQGgVOpdZ(n)
        if n.type == "MIX_RGB":
            xhFRXuXvm(n)
        if n.type == "NORMAL":
            BSOATKOXJ(n)
        if n.type == "NORMAL_MAP":
            BSOATKOXJ_MAP(n)
        if n.type == "OUTPUT_WORLD":
            sDWLNkqJu(n)
        if n.type == "SCRIPT":
            ZCJmKOGzD(n)
        if n.type == "OUTPUT_LINESTYLE":
            plnjKmmtZ(n)
        if n.type == "OUTPUT_LIGHT":
            zzBTDUAVg(n)
        if n.type == "OUTPUT_AOV":
            ckvIUFvtN(n)
        if n.type == "RGB":
            bOQxCWvHm(n)
        if n.type == "CURVE_RGB":
            RdbPbKjVv(n)
        if n.type == "SEPARATE_COLOR":
            vneGQRWoU(n)
        if n.type == "SEPHSV":
            YSZEuczzf(n)
        if n.type == "SEPRGB":
            jwhNRrmPB(n)
        if n.type == "SEPXYZ":
            fqwtkkdRU(n)
        if n.type == "SQUEEZE":
            bkdrnSFkz(n)
        if n.type == "SUBSURFACE_SCATTERING":
            xaptXoRwq(n)
        if n.type == "TANGENT":
            FMldwQBOw(n)
        if n.type == "TEX_WHITE_NOISE":
            wxHxnZfCB(n)
        if n.type == "VALUE":
            BwSZLNVVv(n)
        if n.type == "UVALONGSTROKE":
            mZiPMAZDy(n)
        if n.type == "UVMAP":
            bChYLPtwB(n)
        if n.type == "VERTEX_COLOR":
            wXpKcnCim(n)
        if n.type == "WIREFRAME":
            vdiTKCinc(n)
        if n.type == "WAVELENGTH":
            IjDzchwOP(n)
        if n.type == "VOLUME_SCATTER":
            ftxzoxvsE(n)
        if n.type == "TEX_MAGIC":
            wINzYNwCI(n)
        if n.type == "TEX_IES":
            DkVqqBtQD(n)
        if n.type == "TEX_BRICK":
            jWJZLpVyY(n)
        if n.type == "TEX_POINTDENSITY":
            peVTWBtyH(n)
        if n.type == "TEX_SKY":
            WSPPJWwIb(n)
        if n.type == "TEX_WAVE":
            osEGRoOVD(n)
        if n.type == "TEX_ENVIRONMENT":
            ADegqgvNv(n)
        if n.type == "CURVE_VEC":
            zLETVIVuS(n)
        if n.type == "PRINCIPLED_VOLUME":
            sBXkoWYMx(n)
        if n.type == "VECTOR_DISPLACEMENT":
            PXTujsFmJ(n)
        if n.type == "VECT_MATH":
            niMUoiXCw(n)
        if n.type == "VECTOR_ROTATE":
            sFvwwDRml(n)
        if n.type == "VECT_TRANSFORM":
            dWpnksoez(n)
def export_TEX_IMAGE(n):        
        try:
            imgPath = n.image.filepath
            if '//..' in imgPath:
                imgPath = imgPath.replace('//..', '/home/elinv')
            expPropDic[len(expPropDic)] = {
                "__class__.__name__": n.__class__.__name__,
                "image.filepath": imgPath,
                "image.source": n.image.source,
                "image.colorspace_settings.name": n.image.colorspace_settings.name,
                "image.alpha_mode": n.image.alpha_mode,
                "image_user.frame_current": n.image_user.frame_current,
                "image_user.frame_duration": n.image_user.frame_duration,
                "image_user.frame_offset": n.image_user.frame_offset,
                "image_user.frame_start": n.image_user.frame_start,
                "image_user.tile": n.image_user.tile,
                "image_user.use_auto_refresh": n.image_user.use_auto_refresh,
                "interpolation": n.interpolation,
                "projection": n.projection,
                "projection_blend": n.projection_blend,
                "name": n.name,
            }
        except:
            expPropDic[len(expPropDic)] = {
                "__class__.__name__": n.__class__.__name__,
                "interpolation": n.interpolation,
                "projection": n.projection,
                "projection_blend": n.projection_blend,
                "name": n.name,
            }
            print("Imagen no cargada!")
def export_TEX_COORD(n):
    objVal = None
    try:
        objVal = str(n.object.name)
    except:
        objVal = "null"
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "name": n.name,
        "from_instancer": n.from_instancer,
        "object": objVal,
    }
def cZwbFFCqj(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "name": n.name,
        "vector_type": n.vector_type,
        "inputs['Vector'].default_value": ItLRTKgmf(n.inputs['Vector']),
        "inputs['Location'].default_value": ItLRTKgmf(n.inputs['Location']),
        "inputs['Rotation'].default_value": ItLRTKgmf(n.inputs['Rotation']),
        "inputs['Scale'].default_value": ItLRTKgmf(n.inputs['Scale']),
    }
def gStRTgEJs(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "name": n.name,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "inputs[1].default_value": n.inputs[1].default_value,
        "inputs[2].default_value": n.inputs[2].default_value,
        "inputs[3].default_value": n.inputs[3].default_value,
        "inputs[4].default_value": n.inputs[4].default_value,
        "inputs[6].default_value": n.inputs[6].default_value,
        "subsurface_method": n.subsurface_method,
        "inputs[7].default_value": n.inputs[7].default_value,
        "inputs[8].default_value[0]": n.inputs[8].default_value[0],
        "inputs[8].default_value[1]": n.inputs[8].default_value[1],
        "inputs[8].default_value[2]": n.inputs[8].default_value[2],
        "inputs[9].default_value": n.inputs[9].default_value,
        "inputs[10].default_value": n.inputs[10].default_value,
        "inputs[11].default_value": n.inputs[11].default_value,
        "distribution": n.distribution,
        "inputs[12].default_value": n.inputs[12].default_value,
        "inputs[13].default_value": ODMuAEIrd(n.inputs[13].default_value),
        "inputs[14].default_value": n.inputs[14].default_value,
        "inputs[15].default_value": n.inputs[15].default_value,
        "inputs[17].default_value": n.inputs[17].default_value,
        "inputs[18].default_value": n.inputs[18].default_value,
        "inputs[19].default_value": n.inputs[19].default_value,
        "inputs[20].default_value": n.inputs[20].default_value,
        "inputs[21].default_value": ODMuAEIrd(n.inputs[21].default_value),
        "inputs[23].default_value": n.inputs[23].default_value,
        "inputs[24].default_value": n.inputs[24].default_value,
        "inputs[25].default_value": ODMuAEIrd(n.inputs[25].default_value),
        "inputs[26].default_value": ODMuAEIrd(n.inputs[26].default_value),
        "inputs[27].default_value": n.inputs[27].default_value,
    }
def eIFRbtmOs(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
		"name": n.name,
		"is_active_output": n.is_active_output,
		"target": n.target
    }
def EphkWZNUR(n):
    expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"noise_dimensions": n.noise_dimensions,
        "normalize": n.normalize,
		"inputs[1].default_value": n.inputs[1].default_value,
		"inputs[2].default_value": n.inputs[2].default_value,
		"inputs[3].default_value": n.inputs[3].default_value,
		"inputs[4].default_value": n.inputs[4].default_value,
		"inputs[5].default_value": n.inputs[5].default_value,
		"inputs[6].default_value": n.inputs[6].default_value,
		"name": n.name
    }
def MwMVeYvPY(n):
    expPropDic[len(expPropDic)] = {
		"gradient_type": n.gradient_type,
		"name": n.name,
		"label": n.label,
		"__class__.__name__": n.__class__.__name__
	}
def IwRYgpJRU(n):
    nDic = len(expPropDic)
    expPropDic[nDic] = {
        "__class__.__name__": n.__class__.__name__,
		"color_ramp.interpolation": n.color_ramp.interpolation,
		"color_ramp.color_mode": n.color_ramp.color_mode,
		"inputs[0].default_value": n.inputs[0].default_value,
		"name": n.name,		
	}
    rampElem = len(n.color_ramp.elements)
    countElem = {"countElement": rampElem,}
    expPropDic[nDic].update(countElem)
    for x in range(rampElem):
        elem = {
            "color_ramp.elements[" + str(x) + "].position": n.color_ramp.elements[x].position,
            "color_ramp.elements[" + str(x) + "].color": ODMuAEIrd(n.color_ramp.elements[x].color),
        }
        expPropDic[nDic].update(elem)
def KDwwooecF(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"distribution": n.distribution,
		"inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
		"inputs[1].default_value": n.inputs[1].default_value,
		"inputs[2].default_value": n.inputs[2].default_value,
		"inputs[3].default_value": n.inputs[3].default_value,
		"name": n.name
	}
def QfVExZeiT(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value": n.inputs[0].default_value,
		"name": n.name
	}
def KynjtDIPu(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value": n.inputs[0].default_value,
		"name": n.name
	}
def XVrSIuNrv(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),       #Color
		"inputs[1].default_value": n.inputs[1].default_value,
		"name": n.name
	}
def KjWhAwphM(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),       #Color
		"inputs[1].default_value": n.inputs[1].default_value,
		"name": n.name
	}
def EaQoswpZO(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value": n.inputs[0].default_value,
		"name": n.name
	}          
def OkmOAFOEn(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"invert": n.invert,
		"inputs[0].default_value": n.inputs[0].default_value,
		"inputs[1].default_value": n.inputs[1].default_value,
		"name": n.name
	}
def JrinVafsq(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
		"inputs[1].default_value": n.inputs[1].default_value,
		"name": n.name
	}
def iWCoXXQkW(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[1].default_value": ODMuAEIrd(n.inputs[1].default_value),
		"inputs[2].default_value": ODMuAEIrd(n.inputs[2].default_value),
		"inputs[3].default_value": n.inputs[3].default_value,
		"name": n.name
	}
def bylTZogcQ(n):
    expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"data_type": n.data_type,
		"blend_type": n.blend_type,
		"clamp_result": n.clamp_result,
		"clamp_factor": n.clamp_factor,
		"inputs[0].default_value": n.inputs[0].default_value,
		"inputs[1].default_value[0]": n.inputs[1].default_value[0],
		"inputs[1].default_value[1]": n.inputs[1].default_value[1],
		"inputs[1].default_value[2]": n.inputs[1].default_value[2],
		"inputs[2].default_value": n.inputs[2].default_value,
		"inputs[3].default_value": n.inputs[3].default_value,
		"inputs[4].default_value[0]": n.inputs[4].default_value[0],
		"inputs[4].default_value[1]": n.inputs[4].default_value[1],
		"inputs[4].default_value[2]": n.inputs[4].default_value[2],
		"inputs[5].default_value[0]": n.inputs[5].default_value[0],
		"inputs[5].default_value[1]": n.inputs[5].default_value[1],
		"inputs[5].default_value[2]": n.inputs[5].default_value[2],
		"inputs[6].default_value": ODMuAEIrd(n.inputs[6].default_value),
		"inputs[7].default_value": ODMuAEIrd(n.inputs[7].default_value),
		"name": n.name
	}
def CxbBrQiBS(n):
    expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
		"name": n.name
	}
def qrZytqUAJ(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"musgrave_dimensions": n.musgrave_dimensions,
		"musgrave_type": n.musgrave_type,
		"inputs[1].default_value": n.inputs[1].default_value,
		"inputs[2].default_value": n.inputs[2].default_value,
		"inputs[3].default_value": n.inputs[3].default_value,
		"inputs[4].default_value": n.inputs[4].default_value,
		"inputs[5].default_value": n.inputs[5].default_value,
		"inputs[6].default_value": n.inputs[6].default_value,
		"inputs[7].default_value": n.inputs[7].default_value,
		"name": n.name
	}
def zLLbwwbNS(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"operation": n.operation,
		"use_clamp": n.use_clamp,
		"inputs[0].default_value": n.inputs[0].default_value,
		"inputs[1].default_value": n.inputs[1].default_value,
		"inputs[2].default_value": n.inputs[2].default_value,
		"name": n.name
	}
def lJCKAlCBk(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"voronoi_dimensions": n.voronoi_dimensions,
		"feature": n.feature,
		"distance": n.distance,
		"normalize": n.normalize,
		"inputs[1].default_value": n.inputs[1].default_value,
		"inputs[2].default_value": n.inputs[2].default_value,
		"inputs[3].default_value": n.inputs[3].default_value,
		"inputs[4].default_value": n.inputs[4].default_value,
		"inputs[5].default_value": n.inputs[5].default_value,
		"inputs[6].default_value": n.inputs[6].default_value,
		"inputs[7].default_value": n.inputs[7].default_value,
		"inputs[8].default_value": n.inputs[8].default_value,
		"name": n.name
	}
def yHnMJiCSfMENT(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"space": n.space,
		"inputs[0].default_value": n.inputs[0].default_value,
		"inputs[1].default_value": n.inputs[1].default_value,
		"inputs[2].default_value": n.inputs[2].default_value,
		"name": n.name
	}
def kohGcxBEM(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value": n.inputs[0].default_value,
		"name": n.name
	}
def gVyHoIRcK(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
		"inputs[1].default_value": n.inputs[1].default_value,
		"inputs[2].default_value": n.inputs[2].default_value,
		"name": n.name
	}
def MFZepBrBY(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
		"inputs[1].default_value": n.inputs[1].default_value,
		"name": n.name
	}
def GqeWkiGhY(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"samples": n.samples,
		"inside": n.inside,
		"only_local": n.only_local,
		"inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
		"inputs[1].default_value": n.inputs[1].default_value,
		"name": n.name
	}
def RZrDnQyCc(n):
    print(n.distribution)
    expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"distribution": n.distribution,
		"inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
		"inputs[1].default_value": n.inputs[1].default_value,
		"inputs[2].default_value": n.inputs[2].default_value,
		"name": n.name
	}
def xZFNmztIz(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"component": n.component,
		"inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
		"inputs[1].default_value": n.inputs[1].default_value,
		"inputs[2].default_value": n.inputs[2].default_value,
		"inputs[3].default_value": n.inputs[3].default_value,
		"name": n.name
	}
def xZFNmztIz_PRINCIPLED(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"model": n.model,
		"parametrization": n.parametrization,
		"inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
		"inputs[1].default_value": n.inputs[1].default_value,
		"inputs[2].default_value": n.inputs[2].default_value,
		"inputs[3].default_value": ODMuAEIrd(n.inputs[3].default_value),
		"inputs[4].default_value[0]": n.inputs[4].default_value[0],
		"inputs[4].default_value[1]": n.inputs[4].default_value[1],
		"inputs[4].default_value[2]": n.inputs[4].default_value[2],
		"inputs[5].default_value": n.inputs[5].default_value,
		"inputs[6].default_value": n.inputs[6].default_value,
		"inputs[7].default_value": n.inputs[7].default_value,
		"inputs[8].default_value": n.inputs[8].default_value,
		"inputs[9].default_value": n.inputs[9].default_value,
		"inputs[10].default_value": n.inputs[10].default_value,
		"inputs[11].default_value": n.inputs[11].default_value,
		"inputs[12].default_value": n.inputs[12].default_value,
		"inputs[13].default_value": n.inputs[13].default_value,
		"inputs[14].default_value": n.inputs[14].default_value,
		"inputs[15].default_value": n.inputs[15].default_value,
		"inputs[16].default_value": n.inputs[16].default_value,
		"inputs[17].default_value": n.inputs[17].default_value,
		"name": n.name
	}
def NoMQYIWaf(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"samples": n.samples,
		"inputs[0].default_value": n.inputs[0].default_value,
		"name": n.name
	}
def zZTVDXLkl(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"attribute_type": n.attribute_type,
		"attribute_name": n.attribute_name,
        "name": n.name
	}
def LGHJGbWdT(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"distribution": n.distribution,
		"inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
		"inputs[1].default_value": n.inputs[1].default_value,
		"inputs[2].default_value": n.inputs[2].default_value,
		"name": n.name
	}
def NBjqHyQqA(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"distribution": n.distribution,
		"inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
		"inputs[1].default_value": n.inputs[1].default_value,
		"name": n.name
	}
def pBBcThEHJ(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"component": n.component,
		"inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
		"inputs[1].default_value": n.inputs[1].default_value,
		"inputs[2].default_value": n.inputs[2].default_value,
		"name": n.name
	}
def aCMpWANas(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
		"name": n.name
	}
def ToQBHwBWT(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
		"name": n.name
	}
def RUnAudCpr(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
		"inputs[1].default_value": ODMuAEIrd(n.inputs[1].default_value),
		"inputs[2].default_value": n.inputs[2].default_value,
		"inputs[3].default_value": ODMuAEIrd(n.inputs[3].default_value),
		"inputs[4].default_value": n.inputs[4].default_value,
		"inputs[6].default_value": n.inputs[6].default_value,
		"inputs[7].default_value": n.inputs[7].default_value,
		"name": n.name
	}
def rCCnTnNbv(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value": n.inputs[0].default_value,
		"inputs[1].default_value": n.inputs[1].default_value,
		"inputs[2].default_value": n.inputs[2].default_value,
		"name": n.name
	}
def eFYwbMveu(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value": n.inputs[0].default_value,
		"inputs[1].default_value": n.inputs[1].default_value,
		"inputs[2].default_value": n.inputs[2].default_value,
		"name": n.name
	}
def bqfCDkyQx(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value": n.inputs[0].default_value,
		"inputs[1].default_value": n.inputs[1].default_value,
		"inputs[2].default_value": n.inputs[2].default_value,
		"name": n.name
	}
def wfWwqrVlc(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"clamp_type": n.clamp_type,
		"inputs[0].default_value": n.inputs[0].default_value,
		"inputs[1].default_value": n.inputs[1].default_value,
		"inputs[2].default_value": n.inputs[2].default_value,
		"name": n.name
	}
def jQXBHkVtI(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"mode": n.mode,
		"inputs[0].default_value": n.inputs[0].default_value,
		"inputs[1].default_value": n.inputs[1].default_value,
		"inputs[2].default_value": n.inputs[2].default_value,
		"name": n.name
	}
def kerYxfLer(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value": n.inputs[0].default_value,
		"inputs[1].default_value": n.inputs[1].default_value,
		"name": n.name
	}
def yovKHNxZd(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value": n.inputs[0].default_value,
		"inputs[1].default_value": n.inputs[1].default_value,
		"inputs[2].default_value": n.inputs[2].default_value,
		"inputs[3].default_value": n.inputs[3].default_value,
		"inputs[4].default_value": ODMuAEIrd(n.inputs[4].default_value),
		"name": n.name
	}
def nPnoFLiwy(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value": n.inputs[0].default_value,
		"inputs[1].default_value": ODMuAEIrd(n.inputs[1].default_value),
		"name": n.name
	}
def LlzxgAPQg(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value": n.inputs[0].default_value,
		"inputs[1].default_value": n.inputs[1].default_value,
		"name": n.name
	}
def mQGgVOpdZ(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"data_type": n.data_type,
		"interpolation_type": n.interpolation_type,
		"clamp": n.clamp,         
        "inputs[0].default_value": n.inputs[0].default_value,
        "inputs[1].default_value": n.inputs[1].default_value,
        "inputs[2].default_value": n.inputs[2].default_value,
        "inputs[3].default_value": n.inputs[3].default_value,
        "inputs[4].default_value": n.inputs[4].default_value,
        "inputs[5].default_value": n.inputs[5].default_value,
        "inputs[7].default_value[0]": n.inputs[7].default_value[0],
        "inputs[7].default_value[1]": n.inputs[7].default_value[1],
        "inputs[7].default_value[2]": n.inputs[7].default_value[2],
        "inputs[8].default_value[0]": n.inputs[8].default_value[0],
        "inputs[8].default_value[1]": n.inputs[8].default_value[1],
        "inputs[8].default_value[2]": n.inputs[8].default_value[2],
        "inputs[9].default_value[0]": n.inputs[9].default_value[0],
        "inputs[9].default_value[1]": n.inputs[9].default_value[1],
        "inputs[9].default_value[2]": n.inputs[9].default_value[2],
        "inputs[10].default_value[0]": n.inputs[10].default_value[0],
        "inputs[10].default_value[1]": n.inputs[10].default_value[1],
        "inputs[10].default_value[2]": n.inputs[10].default_value[2],
        "inputs[11].default_value[0]": n.inputs[11].default_value[0],
        "inputs[11].default_value[1]": n.inputs[11].default_value[1],
        "inputs[11].default_value[2]": n.inputs[11].default_value[2],
        "name": n.name
	}
def xhFRXuXvm(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"blend_type": n.blend_type,
		"use_clamp": n.use_clamp,
		"inputs[0].default_value": n.inputs[0].default_value,
		"inputs[1].default_value": ODMuAEIrd(n.inputs[1].default_value),
		"inputs[2].default_value": ODMuAEIrd(n.inputs[2].default_value),
		"name": n.name
	}
def BSOATKOXJ(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"outputs[0].default_value": ItLRTKgmf(n.outputs[0]),
		"inputs[0].default_value": ItLRTKgmf(n.inputs[0]),
		"name": n.name
	}
def BSOATKOXJ_MAP(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"space": n.space,
		"uv_map": n.uv_map,
		"inputs[0].default_value": n.inputs[0].default_value,
		"inputs[1].default_value": ODMuAEIrd(n.inputs[1].default_value),
		"name": n.name
	}
def sDWLNkqJu(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"target": n.target,
		"name": n.name
	}
def ZCJmKOGzD(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"mode": n.mode,
		"script": n.script,
		"filepath": n.filepath,
		"name": n.name
	}
def plnjKmmtZ(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"blend_type": n.blend_type,
        "use_clamp": n.use_clamp,
		"inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
		"inputs[1].default_value": n.inputs[1].default_value,        
		"inputs[2].default_value": n.inputs[2].default_value,
		"inputs[3].default_value": n.inputs[3].default_value,
		"name": n.name
	}
def zzBTDUAVg(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"target": n.target,
		"name": n.name
	}
def ckvIUFvtN(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
		"inputs[1].default_value": n.inputs[1].default_value,
		"name": n.name
	}
def bOQxCWvHm(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"outputs[0].default_value": ODMuAEIrd(n.outputs[0].default_value),
		"name": n.name
	}
def RdbPbKjVv(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value": n.inputs[0].default_value,
		"inputs[1].default_value": ODMuAEIrd(n.inputs[1].default_value),
		"name": n.name
	}
def vneGQRWoU(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"mode": n.mode,
		"inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
		"name": n.name
	}
def YSZEuczzf(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
		"name": n.name
	}
def jwhNRrmPB(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
		"name": n.name
	}
def fqwtkkdRU(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value[0]": n.inputs[0].default_value[0],
		"inputs[0].default_value[1]": n.inputs[0].default_value[1],
		"inputs[0].default_value[2]": n.inputs[0].default_value[2],
		"name": n.name
	}
def bkdrnSFkz(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value": n.inputs[0].default_value,
		"inputs[1].default_value": n.inputs[1].default_value,
		"inputs[2].default_value": n.inputs[2].default_value,
		"name": n.name
	}
def xaptXoRwq(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"falloff": n.falloff,
		"inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
		"inputs[1].default_value": n.inputs[1].default_value,
		"inputs[2].default_value[0]": n.inputs[2].default_value[0],
		"inputs[2].default_value[1]": n.inputs[2].default_value[1],
		"inputs[2].default_value[2]": n.inputs[2].default_value[2],
		"inputs[3].default_value": n.inputs[3].default_value,
		"inputs[4].default_value": n.inputs[4].default_value,
		"name": n.name
	}
def FMldwQBOw(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"direction_type": n.direction_type,
		"axis": n.axis,
		"name": n.name
	}
def wxHxnZfCB(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"noise_dimensions": n.noise_dimensions,
		"name": n.name
	}
def BwSZLNVVv(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"outputs[0].default_value": n.outputs[0].default_value,
		"name": n.name
	}
def mZiPMAZDy(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"use_tips": n.use_tips,
		"name": n.name
	}
def bChYLPtwB(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"from_instancer": n.from_instancer,
		"uv_map": n.uv_map,
		"name": n.name
	}
def wXpKcnCim(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"layer_name": n.layer_name,
		"name": n.name
	}
def vdiTKCinc(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"use_pixel_size": n.use_pixel_size,
		"inputs[0].default_value": n.inputs[0].default_value,
		"name": n.name
	}
def IjDzchwOP(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value": n.inputs[0].default_value,
		"name": n.name
	}
def ftxzoxvsE(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
		"inputs[1].default_value": n.inputs[1].default_value,
		"inputs[2].default_value": n.inputs[2].default_value,
		"name": n.name
	}
def wINzYNwCI(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"turbulence_depth": n.turbulence_depth,
		"inputs[1].default_value": n.inputs[1].default_value,
		"inputs[2].default_value": n.inputs[2].default_value,
		"name": n.name
	}
def DkVqqBtQD(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"mode": n.mode,
		"ies": n.ies,
		"filepath": n.filepath,
		"inputs[1].default_value": n.inputs[1].default_value,
		"name": n.name
	}
def jWJZLpVyY(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"offset": n.offset,
		"offset_frequency": n.offset_frequency,
		"squash": n.squash,
		"squash_frequency": n.squash_frequency,
		"inputs[1].default_value": ODMuAEIrd(n.inputs[1].default_value),
		"inputs[2].default_value": ODMuAEIrd(n.inputs[2].default_value),
		"inputs[3].default_value": ODMuAEIrd(n.inputs[3].default_value),
		"inputs[4].default_value": n.inputs[4].default_value,
		"inputs[5].default_value": n.inputs[5].default_value,
		"inputs[6].default_value": n.inputs[6].default_value,
		"inputs[7].default_value": n.inputs[7].default_value,
		"inputs[8].default_value": n.inputs[8].default_value,
		"inputs[9].default_value": n.inputs[9].default_value,
		"name": n.name
	}
def peVTWBtyH(n):
    objVal = None
    try:
        objVal = str(n.object.name)
    except:
        objVal = "null"
    expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"point_source": n.point_source,
		"object": objVal,
		"space": n.space,
		"radius": n.radius,
		"interpolation": n.interpolation,
		"resolution": n.resolution,
		"particle_color_source": n.particle_color_source,
		"name": n.name
	}
def WSPPJWwIb(n):
    print(n.sun_direction)
    expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"sky_type": n.sky_type,
		"sun_disc": n.sun_disc,
		"sun_size": n.sun_size,
		"sun_intensity": n.sun_intensity,
		"sun_elevation": n.sun_elevation,
		"sun_rotation": n.sun_rotation,
		"altitude": n.altitude,
		"air_density": n.air_density,
		"dust_density": n.dust_density,
		"ozone_density": n.ozone_density,
		"sun_direction": ItLRTKgmf(n.sun_direction),            
		"turbidity": n.turbidity,
		"ground_albedo": n.ground_albedo,
		"name": n.name
	}
def osEGRoOVD(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"wave_type": n.wave_type,
		"bands_direction": n.bands_direction,
		"wave_profile": n.wave_profile,
		"inputs[1].default_value": n.inputs[1].default_value,
		"inputs[2].default_value": n.inputs[2].default_value,
		"inputs[3].default_value": n.inputs[3].default_value,
		"inputs[4].default_value": n.inputs[4].default_value,
		"inputs[5].default_value": n.inputs[5].default_value,
		"inputs[6].default_value": n.inputs[6].default_value,
		"name": n.name
	}
def ADegqgvNv(n):
    try:
        expPropDic[len(expPropDic)] = {
    		"__class__.__name__": n.__class__.__name__,
	    	"interpolation": n.interpolation,
		    "projection": n.projection,
    		"source": n.source,
	    	"colorspace_settings.name": n.colorspace_settings.name,
		    "alpha_mode": n.alpha_mode,
    		"name": n.name
        }
    except:
        expPropDic[len(expPropDic)] = {
            "__class__.__name__": n.__class__.__name__,
            "interpolation": n.interpolation,
            "projection": n.projection,
            "name": n.name
        }
def zLETVIVuS(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value": n.inputs[0].default_value,
		"inputs[1].default_value[0]": n.inputs[1].default_value[0],
		"inputs[1].default_value[1]": n.inputs[1].default_value[1],
		"inputs[1].default_value[2]": n.inputs[1].default_value[2],
		"name": n.name
	}
def sBXkoWYMx(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
		"inputs[1].default_value": n.inputs[1].default_value,
		"inputs[2].default_value": n.inputs[2].default_value,
		"inputs[3].default_value": n.inputs[3].default_value,
		"inputs[4].default_value": n.inputs[4].default_value,
		"inputs[5].default_value": ODMuAEIrd(n.inputs[5].default_value),
		"inputs[6].default_value": n.inputs[6].default_value,
		"inputs[7].default_value": ODMuAEIrd(n.inputs[7].default_value),
		"inputs[8].default_value": n.inputs[8].default_value,
		"inputs[9].default_value": ODMuAEIrd(n.inputs[9].default_value),
		"inputs[10].default_value": n.inputs[10].default_value,
		"inputs[11].default_value": n.inputs[11].default_value,
		"name": n.name
	}
def PXTujsFmJ(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"space": n.space,
		"inputs[1].default_value": n.inputs[1].default_value,
		"inputs[2].default_value": n.inputs[2].default_value,
		"name": n.name
	}
def niMUoiXCw(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"operation": n.operation,
		"inputs[0].default_value[0]": n.inputs[0].default_value[0],
		"inputs[0].default_value[1]": n.inputs[0].default_value[1],
		"inputs[0].default_value[2]": n.inputs[0].default_value[2],
		"inputs[1].default_value[0]": n.inputs[1].default_value[0],
		"inputs[1].default_value[1]": n.inputs[1].default_value[1],
		"inputs[1].default_value[2]": n.inputs[1].default_value[2],
		"inputs[2].default_value[0]": n.inputs[2].default_value[0],
		"inputs[2].default_value[1]": n.inputs[2].default_value[1],
		"inputs[2].default_value[2]": n.inputs[2].default_value[2],
		"inputs[3].default_value": n.inputs[3].default_value,
		"name": n.name
	}
def sFvwwDRml(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"rotation_type": n.rotation_type,
		"invert": n.invert,
		"inputs[1].default_value[0]": n.inputs[1].default_value[0],
		"inputs[1].default_value[1]": n.inputs[1].default_value[1],
		"inputs[1].default_value[2]": n.inputs[1].default_value[2],
		"inputs[2].default_value[0]": n.inputs[2].default_value[0],
		"inputs[2].default_value[1]": n.inputs[2].default_value[1],
		"inputs[2].default_value[2]": n.inputs[2].default_value[2],
		"inputs[3].default_value": n.inputs[3].default_value,
		"inputs[4].default_value[0]": n.inputs[4].default_value[0],
		"inputs[4].default_value[1]": n.inputs[4].default_value[1],
		"inputs[4].default_value[2]": n.inputs[4].default_value[2],
		"name": n.name
	}
def dWpnksoez(n):
	expPropDic[len(expPropDic)] = {
		"__class__.__name__": n.__class__.__name__,
		"vector_type": n.vector_type,
		"convert_from": n.convert_from,
		"convert_to": n.convert_to,
		"inputs[0].default_value[0]": n.inputs[0].default_value[0],
		"inputs[0].default_value[1]": n.inputs[0].default_value[1],
		"inputs[0].default_value[2]": n.inputs[0].default_value[2],
		"name": n.name
	}	
