import bpy, os
expLinksDic = {}
expPropDic = {}
nodosDic = {}
def ItLRTKgmf(node, enum: str = "") -> str:
    vectColor = node.default_value
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
def gehFagdSM(vect):
    return f"({vect[0]}, {vect[1]}, {vect[2]})"
def AtisvxdBx(n, nodes):
    for n in nodes:
        if n.type == "VIEWER":
            fCGBzVRRj(n)
        if n.type == "COMPOSITE":
            hybQFtQwz(n)
        if n.type == "R_LAYERS":
             yxiYhtZtG(n)
        if n.type == "IMAGE":
             ZSiRzmpfG(n)
        if n.type == "ALPHAOVER":
             DYilfiYca(n)
        if n.type == "SCALE":
             YaZtKyRuJ(n)
        if n.type == "COMBRGBA":
            owRhjBSEq(n)
        if n.type == "COMBYCCA":
            SaSAITxSp(n)
        if n.type == "COMBYUVA":
            IbDLNNDfD(n)
        if n.type == "COMBINE_COLOR":                
            jQXBHkVtI(n)
        if n.type == "COMBHSVA":
            iaOtwqdiI(n)
        if n.type == "COMBINE_XYZ":
            uOhxmgYxi(n)
        if n.type == "VALUE":
            BwSZLNVVv(n)
        if n.type == "NORMALIZE":
            JdHqdrjCk(n)
        if n.type == "VIEWSWITCH":
            IviWIWQKx(n)
        if n.type == "MATH":
            zLLbwwbNS(n)
        if n.type == "ID_MASK":
            iwYFTdWtn(n)
        if n.type == "LEVELS":
            vFUtAvwOs(n)
        if n.type == "NORMALIZE":
            JdHqdrjCk(n)
        if n.type == "VALUE":
            BwSZLNVVv(n)
        if n.type == "SEPARATE_XYZ":
            mSdKMffoj(n)
        if n.type == "OUTPUT_FILE":
            yeczhqhyH(n)
        if n.type == "MASK":
            HspshVefJ(n)
        if n.type == "DILATEERODE":
            RnqTvYzXp(n)
        if n.type == "MAP_RANGE":
            mQGgVOpdZ(n)
        if n.type == "MAP_VALUE":
            jIPcbnLrE(n)
        if n.type == "DOUBLEEDGEMASK":
            VAgJxVxGm(n)
        if n.type == "ELLIPSEMASK":
            bFCywmEMI(n)
        if n.type == "CURVE_VEC":
            zLETVIVuS(n)
        if n.type == "TIME":
            boxGYHLpY(n)
        if n.type == "CRYPTOMATTE":
            qGYuEheWK(n)
        if n.type == "BOXMASK":
            uNdZmThvo(n)
        if n.type == "TRACKPOS":
            wVpXeckaL(n)
        if n.type == "MOVIECLIP":
            CrLrhKOBz(n)
        if n.type == "CRYPTOMATTE_V2":
            qGYuEheWK_V2(n)
        if n.type == "ANTIALIASING":
                mSzWcaiKL(n)
        if n.type == "BILATERALBLUR":
                GKoRdOsZF(n)
        if n.type == "CHROMA_MATTE":
                YSpyaLiyS(n)
        if n.type == "COLOR_MATTE":
                gkrJYefQl(n)
        if n.type == "RGBTOBW":
                CxbBrQiBS(n)
        if n.type == "SEPYUVA":
                XLsZFDNVy(n)
        if n.type == "SEPHSVA":
                XGeoRDoed(n)
        if n.type == "SEPRGBA":
                kddbZOoZy(n)
        if n.type == "BRIGHTCONTRAST":
                gVyHoIRcK(n)
        if n.type == "BOKEHBLUR":
                ydrOLQfRw(n)
        if n.type == "BLUR":
            XShpCLCpN(n)
        if n.type == "CHANNEL_MATTE":
            GvLzSEmZe(n)
        if n.type == "COLOR_SPILL":
            onZLhFAxL(n)
        if n.type == "BOKEHIMAGE":
            WRPRTFqFp(n)
        if n.type == "COLORBALANCE":
            gKInmHVcd(n)
        if n.type == "COLORCORRECTION":
            tvSAmdQZO(n)
        if n.type == "CONVERT_COLORSPACE":
            VjuYqOnAd(n)
        if n.type == "CROP":
            MMLgsnoud(n)
        if n.type == "DISPLACE":
            yHnMJiCSf(n)
        if n.type == "DIFF_MATTE":
                bojLXEkef(n)
        if n.type == "CORNERPIN":
                savyfCUPf(n)
        if n.type == "DBLUR":
                RoMfPaTmv(n)
        if n.type == "DEFOCUS":
                vQEmHmXtN(n)
        if n.type == "DENOISE":
                ndccXNlXQ(n)
        if n.type == "EXPOSURE":
                FwHyvLHEL(n)
        if n.type == "FILTER":
                PouogcFOt(n)
        if n.type == "DESPECKLE":
                hpLabDWUz(n)
        if n.type == "CURVE_RGB":
                RdbPbKjVv(n)
        if n.type == "DISTANCE_MATTE":
                VZGHjqIXT(n)
        if n.type == "FLIP":
                ENjhQMcHH(n)
        if n.type == "GAMMA":
                JrinVafsq(n)
        if n.type == "GLARE":
                GFZzIDCfT(n)
        if n.type == "HUECORRECT":
                AACNUoHNd(n)
        if n.type == "HUE_SAT":
                yovKHNxZd(n)
        if n.type == "LUMA_MATTE":
                PDWTEhPwg(n)
        if n.type == "KEYING":
                NtFkyjYCL(n)
        if n.type == "INPAINT":
                VidGdWZAk(n)
        if n.type == "MAP_UV":
                rlFZEOanm(n)
        if n.type == "LENSDIST":
                zfqqAMtor(n)
        if n.type == "MIX_RGB":
                xhFRXuXvm(n)
        if n.type == "INVERT":
                nPnoFLiwy(n)
        if n.type == "MOVIEDISTORTION":
                ZtLqxBDyF(n)
        if n.type == "KUWAHARA":
                cGTLYGXfa(n)
        if n.type == "PLANETRACKDEFORM":
                VjpMUbtxc(n)
        if n.type == "NORMAL":
                BSOATKOXJ(n)
        if n.type == "PREMULKEY":
                eUVMRvHDQ(n)
        if n.type == "PIXELATE":
                xLcgjehpb(n)
        if n.type == "TRANSLATE":
                lFAXPNugl(n)
        if n.type == "SPLITVIEWER":
                xXdviXfvv(n)
        if n.type == "VECBLUR":
                KzvcQOlgo(n)
        if n.type == "VALTORGB":
                IwRYgpJRU(n)
        if n.type == "RGB":
                bOQxCWvHm(n)
        if n.type == "SEPARATE_COLOR":
                vneGQRWoU(n)
        if n.type == "TONEMAP":
                hkiyvzmrt(n)
        if n.type == "SUNBEAMS":
                pNeadUytk(n)
        if n.type == "SETALPHA":
                xjNzGMKOU(n)
        if n.type == "SEPYCCA":
                IlfeBiuXV(n)
        if n.type == "STABILIZE2D":
                rFLxSGCUh(n)
        if n.type == "TEXTURE":
                jBSIJuyCa(n)
        if n.type == "ROTATE":
                hsYturPuC(n)
        if n.type == "TRANSFORM":
                DiQJPHEUf(n)
        if n.type == "SWITCH":
                uLIVhdAem(n)
        if n.type == "ZCOMBINE":
                sWFDpGeQa(n)
def fCGBzVRRj(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "name": n.name,
        "use_alpha": n.use_alpha,
        "inputs[1].default_value": n.inputs[1].default_value,
    }
def hybQFtQwz(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "name": n.name,
        "use_alpha": n.use_alpha,
        "inputs[1].default_value": n.inputs[1].default_value,
    }
def yxiYhtZtG(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "name": n.name,
        "layer": n.layer,
        "name": n.name
    }
def ZSiRzmpfG(n):
    try:
        expPropDic[len(expPropDic)] = {
            "__class__.__name__": n.__class__.__name__,
            "source": n.source,
            "colorspace_settings.name": n.colorspace_settings.name,
            "alpha_mode": n.alpha_mode,
            "name": n.name
        }
    except:
        expPropDic[len(expPropDic)] = {
            "__class__.__name__": n.__class__.__name__,
            "name": n.name
        }
def DYilfiYca(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "use_premultiply": n.use_premultiply,
        "premul": n.premul,
        "inputs[0].default_value": n.inputs[0].default_value,
        "name": n.name
    }         
def YaZtKyRuJ(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "space": n.space,
        "frame_method": n.frame_method,
        "offset_y": n.offset_y,
        "offset_x": n.offset_x,
        "name": n.name
    }
def owRhjBSEq(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": n.inputs[0].default_value,
        "inputs[1].default_value": n.inputs[1].default_value,
        "inputs[2].default_value": n.inputs[2].default_value,
        "inputs[3].default_value": n.inputs[3].default_value,
        "name": n.name
    }
def SaSAITxSp(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": n.inputs[0].default_value,
        "inputs[1].default_value": n.inputs[1].default_value,
        "inputs[2].default_value": n.inputs[2].default_value,
        "inputs[3].default_value": n.inputs[3].default_value,
        "name": n.name
    }
def IbDLNNDfD(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": n.inputs[0].default_value,
        "inputs[1].default_value": n.inputs[1].default_value,
        "inputs[2].default_value": n.inputs[2].default_value,
        "inputs[3].default_value": n.inputs[3].default_value,
        "name": n.name
    }
def jQXBHkVtI(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": n.inputs[0].default_value,
        "inputs[1].default_value": n.inputs[1].default_value,
        "inputs[2].default_value": n.inputs[2].default_value,
        "inputs[3].default_value": n.inputs[3].default_value,
        "ycc_mode": n.ycc_mode,
        "name": n.name
    }
def iaOtwqdiI(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": n.inputs[0].default_value,
        "inputs[1].default_value": n.inputs[1].default_value,
        "inputs[2].default_value": n.inputs[2].default_value,
        "inputs[3].default_value": n.inputs[3].default_value,
        "name": n.name
    }
def uOhxmgYxi(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": n.inputs[0].default_value,
        "inputs[1].default_value": n.inputs[1].default_value,
        "inputs[2].default_value": n.inputs[2].default_value,
        "name": n.name
    }
def BwSZLNVVv(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "outputs[0].default_value": n.outputs[0].default_value,
        "name": n.name
    }
def JdHqdrjCk(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": n.inputs[0].default_value,
        "name": n.name
    }
def IviWIWQKx(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "inputs[1].default_value": ODMuAEIrd(n.inputs[1].default_value),
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
def iwYFTdWtn(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "index": n.index,
        "use_antialiasing": n.use_antialiasing,
        "inputs[0].default_value": n.inputs[0].default_value,
        "name": n.name
    }
def vFUtAvwOs(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "channel": n.channel,
        "name": n.name
    }
def JdHqdrjCk(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": n.inputs[0].default_value,
        "name": n.name
    }
def BwSZLNVVv(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "outputs[0].default_value": n.outputs[0].default_value,
        "name": n.name
    }
def mSdKMffoj(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value[0]": n.inputs[0].default_value[0],
        "inputs[0].default_value[1]": n.inputs[0].default_value[1],
        "inputs[0].default_value[2]": n.inputs[0].default_value[2],
        "name": n.name
    }
def yeczhqhyH(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "base_path": n.base_path,
        "name": n.name
    }
def HspshVefJ(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "size_source": n.size_source,
        "use_motion_blur": n.use_motion_blur,
        "name": n.name
    }
def RnqTvYzXp(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "mode": n.mode,
        "distance": n.distance,
        "inputs[0].default_value": n.inputs[0].default_value,
        "name": n.name
    }
def mQGgVOpdZ(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "use_clamp": n.use_clamp,
        "inputs[0].default_value": n.inputs[0].default_value,
        "inputs[1].default_value": n.inputs[1].default_value,
        "inputs[2].default_value": n.inputs[2].default_value,
        "inputs[3].default_value": n.inputs[3].default_value,
        "inputs[4].default_value": n.inputs[4].default_value,
        "name": n.name
    }
def jIPcbnLrE(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "offset[0]": n.offset[0],
        "size[0]": n.size[0],
        "use_min": n.use_min,
        "min[0]": n.min[0],
        "use_max": n.use_max,
        "max[0]": n.max[0],
        "inputs[0].default_value": n.inputs[0].default_value,
        "name": n.name
    }
def VAgJxVxGm(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inner_mode": n.inner_mode,
        "edge_mode": n.edge_mode,
        "inputs[0].default_value": n.inputs[0].default_value,
        "inputs[1].default_value": n.inputs[1].default_value,
        "name": n.name
    }
def bFCywmEMI(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "x": n.x,
        "y": n.y,
        "width": n.width,
        "height": n.height,
        "rotation": n.rotation,
        "mask_type": n.mask_type,
        "inputs[0].default_value": n.inputs[0].default_value,
        "inputs[1].default_value": n.inputs[1].default_value,
        "name": n.name
    }
def zLETVIVuS(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value[0]": n.inputs[0].default_value[0],
        "inputs[0].default_value[1]": n.inputs[0].default_value[1],
        "inputs[0].default_value[2]": n.inputs[0].default_value[2],
        "name": n.name
    }
def boxGYHLpY(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "frame_start": n.frame_start,
        "frame_end": n.frame_end,
        "name": n.name
    }
def qGYuEheWK(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "matte_id": n.matte_id,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "inputs[1].default_value": ODMuAEIrd(n.inputs[1].default_value),
        "inputs[2].default_value": ODMuAEIrd(n.inputs[2].default_value),
        "inputs[3].default_value": ODMuAEIrd(n.inputs[3].default_value),
        "name": n.name
    }
def uNdZmThvo(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "x": n.x,
        "y": n.y,
        "width": n.width,
        "height": n.height,
        "rotation": n.rotation,
        "mask_type": n.mask_type,
        "inputs[0].default_value": n.inputs[0].default_value,
        "inputs[1].default_value": n.inputs[1].default_value,
        "name": n.name
    }
def wVpXeckaL(n):
    try:
        expPropDic[len(expPropDic)] = {
            "__class__.__name__": n.__class__.__name__,
            "tracking_object": n.tracking_object,
            "track_name": n.track_name,
            "position": n.position,
            "video": bpy.path.abspath(n.clip.filepath),
            "name": n.name,
        }
    except:
        expPropDic[len(expPropDic)] = {
            "__class__.__name__": n.__class__.__name__,
            "tracking_object": n.tracking_object,
            "track_name": n.track_name,
            "position": n.position,
            "name": n.name,
        }
def CrLrhKOBz(n):
    try:
        expPropDic[len(expPropDic)] = {
            "__class__.__name__": n.__class__.__name__,
            "video": bpy.path.abspath(n.clip.filepath),
            "name": n.name,
        }
    except:
        expPropDic[len(expPropDic)] = {
            "__class__.__name__": n.__class__.__name__,
            "name": n.name,
        }
def qGYuEheWK_V2(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "source": n.source,
        "layer_name": n.layer_name,
        "matte_id": n.matte_id,
        "name": n.name
    }
def mSzWcaiKL(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "threshold": n.threshold,
        "contrast_limit": n.contrast_limit,
        "corner_rounding": n.corner_rounding,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "name": n.name
    }
def GKoRdOsZF(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "iterations": n.iterations,
        "sigma_color": n.sigma_color,
        "sigma_space": n.sigma_space,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "inputs[1].default_value": ODMuAEIrd(n.inputs[1].default_value),
        "name": n.name
    }
def YSpyaLiyS(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "tolerance": n.tolerance,
        "threshold": n.threshold,
        "gain": n.gain,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "inputs[1].default_value": ODMuAEIrd(n.inputs[1].default_value),
        "name": n.name
    }
def gkrJYefQl(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "color_hue": n.color_hue,
        "color_saturation": n.color_saturation,
        "color_value": n.color_value,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "inputs[1].default_value": ODMuAEIrd(n.inputs[1].default_value),
        "name": n.name
    }
def CxbBrQiBS(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "name": n.name
    }
def XLsZFDNVy(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "name": n.name
    }
def XGeoRDoed(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "name": n.name
    }
def kddbZOoZy(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "name": n.name
    }
def gVyHoIRcK(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "use_premultiply": n.use_premultiply,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "inputs[1].default_value": n.inputs[1].default_value,
        "inputs[2].default_value": n.inputs[2].default_value,
        "name": n.name
    }
def ydrOLQfRw(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "use_variable_size": n.use_variable_size,
        "blur_max": n.blur_max,
        "use_extended_bounds": n.use_extended_bounds,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "inputs[1].default_value": ODMuAEIrd(n.inputs[1].default_value),
        "inputs[2].default_value": n.inputs[2].default_value,
        "inputs[3].default_value": n.inputs[3].default_value,
        "name": n.name
    }
def XShpCLCpN(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "filter_type": n.filter_type,
        "use_variable_size": n.use_variable_size,
        "use_bokeh": n.use_bokeh,
        "use_gamma_correction": n.use_gamma_correction,
        "use_relative": n.use_relative,
        "size_x": n.size_x,
        "size_y": n.size_y,
        "use_extended_bounds": n.use_extended_bounds,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "inputs[1].default_value": n.inputs[1].default_value,
        "name": n.name
    }
def GvLzSEmZe(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "color_space": n.color_space,
        "matte_channel": n.matte_channel,
        "limit_method": n.limit_method,
        "limit_max": n.limit_max,
        "limit_min": n.limit_min,
        "limit_channel": n.limit_channel,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "name": n.name
    }
def onZLhFAxL(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "channel": n.channel,
        "limit_method": n.limit_method,
        "limit_channel": n.limit_channel,
        "ratio": n.ratio,
        "use_unspill": n.use_unspill,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "inputs[1].default_value": n.inputs[1].default_value,
        "name": n.name
    }
def WRPRTFqFp(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "flaps": n.flaps,
        "angle": n.angle,
        "rounding": n.rounding,
        "catadioptric": n.catadioptric,
        "shift": n.shift,
        "name": n.name
    }
def gKInmHVcd(n):
    print(n.lift)
    print(n.inputs[1].default_value)
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "correction_method": n.correction_method,
        "lift": gehFagdSM(n.lift),
        "gamma": gehFagdSM(n.gamma),
        "gain": gehFagdSM(n.gain),
        "offset": gehFagdSM(n.offset),
        "power": gehFagdSM(n.power),
        "slope": gehFagdSM(n.slope),
        "offset_basis": n.offset_basis,
        "inputs[0].default_value": n.inputs[0].default_value,
        "inputs[1].default_value": ODMuAEIrd(n.inputs[1].default_value),
        "name": n.name
    }
def tvSAmdQZO(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "red": n.red,
        "green": n.green,
        "blue": n.blue,
        "master_saturation": n.master_saturation,
        "highlights_saturation": n.highlights_saturation,
        "midtones_saturation": n.midtones_saturation,
        "shadows_saturation": n.shadows_saturation,
        "master_contrast": n.master_contrast,
        "highlights_contrast": n.highlights_contrast,
        "midtones_contrast": n.midtones_contrast,
        "shadows_contrast": n.shadows_contrast,
        "master_gamma": n.master_gamma,
        "highlights_gamma": n.highlights_gamma,
        "midtones_gamma": n.midtones_gamma,
        "shadows_gamma": n.shadows_gamma,
        "master_gain": n.master_gain,
        "highlights_gain": n.highlights_gain,
        "midtones_gain": n.midtones_gain,
        "shadows_gain": n.shadows_gain,
        "master_lift": n.master_lift,
        "highlights_lift": n.highlights_lift,
        "midtones_lift": n.midtones_lift,
        "shadows_lift": n.shadows_lift,
        "midtones_start": n.midtones_start,
        "midtones_end": n.midtones_end,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "inputs[1].default_value": n.inputs[1].default_value,
        "name": n.name
    }
def VjuYqOnAd(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "from_color_space": n.from_color_space,
        "to_color_space": n.to_color_space,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "name": n.name
    }
def MMLgsnoud(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "use_crop_size": n.use_crop_size,
        "relative": n.relative,
        "min_x": n.min_x,
        "max_x": n.max_x,
        "min_y": n.min_y,
        "max_y": n.max_y,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "name": n.name
    }
def yHnMJiCSf(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "inputs[1].default_value[0]": n.inputs[1].default_value[0],
        "inputs[1].default_value[1]": n.inputs[1].default_value[1],
        "inputs[1].default_value[2]": n.inputs[1].default_value[2],
        "inputs[2].default_value": n.inputs[2].default_value,
        "inputs[3].default_value": n.inputs[3].default_value,
        "name": n.name
    }
def bojLXEkef(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "inputs[1].default_value": ODMuAEIrd(n.inputs[1].default_value),
        "tolerance": n.tolerance,
        "falloff": n.falloff,
        "name": n.name
    }
def savyfCUPf(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "inputs[1].default_value[0]": n.inputs[1].default_value[0],
        "inputs[1].default_value[1]": n.inputs[1].default_value[1],
        "inputs[1].default_value[2]": n.inputs[1].default_value[2],
        "inputs[2].default_value[0]": n.inputs[2].default_value[0],
        "inputs[2].default_value[1]": n.inputs[2].default_value[1],
        "inputs[2].default_value[2]": n.inputs[2].default_value[2],
        "inputs[3].default_value[0]": n.inputs[3].default_value[0],
        "inputs[3].default_value[1]": n.inputs[3].default_value[1],
        "inputs[3].default_value[2]": n.inputs[3].default_value[2],
        "inputs[4].default_value[0]": n.inputs[4].default_value[0],
        "inputs[4].default_value[1]": n.inputs[4].default_value[1],
        "inputs[4].default_value[2]": n.inputs[4].default_value[2],
        "name": n.name
    }
def RoMfPaTmv(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "iterations": n.iterations,
        "center_x": n.center_x,
        "center_y": n.center_y,
        "distance": n.distance,
        "angle": n.angle,
        "spin": n.spin,
        "zoom": n.zoom,
        "name": n.name
    }
def vQEmHmXtN(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "bokeh": n.bokeh,
        "angle": n.angle,
        "use_gamma_correction": n.use_gamma_correction,
        "f_stop": n.f_stop,
        "blur_max": n.blur_max,
        "threshold": n.threshold,
        "use_preview": n.use_preview,
        "use_zbuffer": n.use_zbuffer,
        "z_scale": n.z_scale,
        "inputs[1].default_value": n.inputs[1].default_value,
        "name": n.name
    }
def ndccXNlXQ(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "prefilter": n.prefilter,
        "use_hdr": n.use_hdr,
        "name": n.name
    }
def FwHyvLHEL(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "inputs[1].default_value": n.inputs[1].default_value,
        "name": n.name
    }
def PouogcFOt(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[1].default_value": ODMuAEIrd(n.inputs[1].default_value),
        "inputs[0].default_value": n.inputs[0].default_value,
        "filter_type": n.filter_type,
        "name": n.name
    }
def hpLabDWUz(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[1].default_value": ODMuAEIrd(n.inputs[1].default_value),
        "threshold": n.threshold,
        "threshold_neighbor": n.threshold_neighbor,
        "inputs[0].default_value": n.inputs[0].default_value,
        "name": n.name
    }
def RdbPbKjVv(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[1].default_value": ODMuAEIrd(n.inputs[1].default_value),
        "inputs[2].default_value": ODMuAEIrd(n.inputs[2].default_value),
        "inputs[3].default_value": ODMuAEIrd(n.inputs[3].default_value),
        "inputs[0].default_value": n.inputs[0].default_value,
        "name": n.name
    }
def VZGHjqIXT(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "inputs[1].default_value": ODMuAEIrd(n.inputs[1].default_value),
        "tolerance": n.tolerance,
        "falloff": n.falloff,
        "channel": n.channel,
        "channel": n.channel,
        "name": n.name
    }
def ENjhQMcHH(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "axis": n.axis,
        "name": n.name
    }
def JrinVafsq(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "inputs[1].default_value": n.inputs[1].default_value,
        "name": n.name
    }
def GFZzIDCfT(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "glare_type": n.glare_type,
        "quality": n.quality,
        "iterations": n.iterations,
        "color_modulation": n.color_modulation,
        "mix": n.mix,
        "threshold": n.threshold,
        "streaks": n.streaks,
        "angle_offset": n.angle_offset,
        "fade": n.fade,
        "name": n.name
    }
def AACNUoHNd(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[1].default_value": ODMuAEIrd(n.inputs[1].default_value),
        "inputs[0].default_value": n.inputs[0].default_value,
        "name": n.name
    }
def yovKHNxZd(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "inputs[1].default_value": n.inputs[1].default_value,
        "inputs[2].default_value": n.inputs[2].default_value,
        "inputs[3].default_value": n.inputs[3].default_value,
        "inputs[4].default_value": n.inputs[4].default_value,
        "name": n.name
    }
def PDWTEhPwg(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "limit_max": n.limit_max,
        "limit_min": n.limit_min,
        "name": n.name
    }
def NtFkyjYCL(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "inputs[1].default_value": ODMuAEIrd(n.inputs[1].default_value),
        "blur_pre": n.blur_pre,
        "screen_balance": n.screen_balance,
        "despill_factor": n.despill_factor,
        "despill_balance": n.despill_balance,
        "edge_kernel_radius": n.edge_kernel_radius,
        "edge_kernel_tolerance": n.edge_kernel_tolerance,
        "clip_black": n.clip_black,
        "clip_white": n.clip_white,
        "dilate_distance": n.dilate_distance,
        "feather_falloff": n.feather_falloff,
        "feather_distance": n.feather_distance,
        "blur_post": n.blur_post,
        "name": n.name
    }
def VidGdWZAk(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "distance": n.distance,
        "name": n.name
    }
def rlFZEOanm(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "alpha": n.alpha,
        "inputs[1].default_value[0]": n.inputs[1].default_value[0],
        "inputs[1].default_value[1]": n.inputs[1].default_value[1],
        "inputs[1].default_value[2]": n.inputs[1].default_value[2],
        "name": n.name
    }
def zfqqAMtor(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "use_projector": n.use_projector,
        "use_jitter": n.use_jitter,
        "use_fit": n.use_fit,
        "inputs[1].default_value": n.inputs[1].default_value,
        "inputs[2].default_value": n.inputs[2].default_value,
        "name": n.name
    }
def xhFRXuXvm(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[1].default_value": ODMuAEIrd(n.inputs[1].default_value),
        "inputs[2].default_value": ODMuAEIrd(n.inputs[2].default_value),
        "blend_type": n.blend_type,
        "use_clamp": n.use_clamp,
        "inputs[0].default_value": n.inputs[0].default_value,
        "use_alpha": n.use_alpha,
        "name": n.name
    }
def nPnoFLiwy(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[1].default_value": ODMuAEIrd(n.inputs[1].default_value),
        "invert_rgb": n.invert_rgb,
        "invert_alpha": n.invert_alpha,
        "inputs[0].default_value": n.inputs[0].default_value,
        "name": n.name
    }
def ZtLqxBDyF(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "distortion_type": n.distortion_type,
        "name": n.name
    }
def cGTLYGXfa(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "variation": n.variation,
        "size": n.size,
        "uniformity": n.uniformity,
        "sharpness": n.sharpness,
        "eccentricity": n.eccentricity,
        "name": n.name
    }
def VjpMUbtxc(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "use_motion_blur": n.use_motion_blur,
        "tracking_object": n.tracking_object,
        "plane_track_name": n.plane_track_name,
        "name": n.name
    }
def BSOATKOXJ(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "outputs[0].default_value": ItLRTKgmf(n.outputs[0]),
        "inputs[0].default_value": ItLRTKgmf(n.inputs[0]),
        "name": n.name
    }
def eUVMRvHDQ(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "mapping": n.mapping,
        "name": n.name
    }
def xLcgjehpb(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "name": n.name
    }
def lFAXPNugl(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "inputs[1].default_value": n.inputs[1].default_value,
        "inputs[2].default_value": n.inputs[2].default_value,
        "use_relative": n.use_relative,
        "wrap_axis": n.wrap_axis,
        "name": n.name
    }
def xXdviXfvv(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "inputs[1].default_value": ODMuAEIrd(n.inputs[1].default_value),
        "axis": n.axis,
        "factor": n.factor,
        "name": n.name
    }
def KzvcQOlgo(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "inputs[1].default_value": n.inputs[1].default_value,
        "inputs[2].default_value[0]": n.inputs[2].default_value[0],
        "inputs[2].default_value[1]": n.inputs[2].default_value[1],
        "inputs[2].default_value[2]": n.inputs[2].default_value[2],
        "use_curved": n.use_curved,
        "samples": n.samples,
        "factor": n.factor,
        "speed_min": n.speed_min,
        "speed_max": n.speed_max,
        "name": n.name
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
def bOQxCWvHm(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "outputs[0].default_value": ODMuAEIrd(n.outputs[0].default_value),
        "name": n.name
    }
def vneGQRWoU(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "mode": n.mode,
        "ycc_mode": n.ycc_mode,
        "name": n.name
    }
def hkiyvzmrt(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "tonemap_type": n.tonemap_type,
        "intensity": n.intensity,
        "contrast": n.contrast,
        "adaptation": n.adaptation,
        "correction": n.correction,
        "key": n.key,
        "offset": n.offset,
        "gamma": n.gamma,
        "name": n.name
    }
def pNeadUytk(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "source[0]": n.source[0],
        "source[1]": n.source[1],
        "ray_length": n.ray_length,
        "name": n.name
    }
def xjNzGMKOU(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "inputs[1].default_value": n.inputs[1].default_value,
        "mode": n.mode,
        "name": n.name
    }
def IlfeBiuXV(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "mode": n.mode,
        "name": n.name
    }
def rFLxSGCUh(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "invert": n.invert,
        "filter_type": n.filter_type,
        "name": n.name
    }
def jBSIJuyCa(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "texture": n.texture,
        "inputs[0].default_value[0]": n.inputs[0].default_value[0],
        "inputs[0].default_value[1]": n.inputs[0].default_value[1],
        "inputs[0].default_value[2]": n.inputs[0].default_value[2],
        "inputs[1].default_value[0]": n.inputs[1].default_value[0],
        "inputs[1].default_value[1]": n.inputs[1].default_value[1],
        "inputs[1].default_value[2]": n.inputs[1].default_value[2],
        "name": n.name
    }
def hsYturPuC(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "inputs[1].default_value": n.inputs[1].default_value,
        "filter_type": n.filter_type,
        "name": n.name
    }
def DiQJPHEUf(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "filter_type": n.filter_type,
        "inputs[1].default_value": n.inputs[1].default_value,
        "inputs[2].default_value": n.inputs[2].default_value,
        "inputs[3].default_value": n.inputs[3].default_value,
        "inputs[4].default_value": n.inputs[4].default_value,
        "name": n.name
    }
def uLIVhdAem(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "inputs[1].default_value": ODMuAEIrd(n.inputs[1].default_value),
        "check": n.check,
        "name": n.name
    }
def sWFDpGeQa(n):
    expPropDic[len(expPropDic)] = {
        "__class__.__name__": n.__class__.__name__,
        "inputs[0].default_value": ODMuAEIrd(n.inputs[0].default_value),
        "inputs[2].default_value": ODMuAEIrd(n.inputs[2].default_value),
        "use_alpha": n.use_alpha,
        "use_antialias_z": n.use_antialias_z,
        "inputs[1].default_value": n.inputs[1].default_value,
        "inputs[3].default_value": n.inputs[3].default_value,
        "name": n.name
    }
