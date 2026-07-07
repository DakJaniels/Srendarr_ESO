-- ////// START : GENERATED FROM Srendarr/Srendarr.xml
---------- LVL: 00 ----------
---------- LVL: 01 ----------
---------- LVL: 02 ----------
-- ---------------------------------------------------------------------------------------------------------------------
--
---@class Srendarr : TopLevelWindow
Srendarr = {}
-- ---------------------------------------------------------------------------------------------------------------------
--
---@class Srendarr_CastBar : TopLevelWindow
---@field public hidden boolean
---@field public clampedToScreen boolean
Srendarr_CastBar = {}
-- ---------------------------------------------------------------------------------------------------------------------
--
---@class Srendarr_GroupAuras : TopLevelWindow
---@field public tier DrawTier
---@field public mouseEnabled boolean
---@field public movable boolean
---@field public clampedToScreen boolean
---@field public hidden boolean
---@field Dimensions {x: layout_measurement, y: layout_measurement}
---@field Anchor {point: AnchorPosition}
Srendarr_GroupAuras = {}
-- ---------------------------------------------------------------------------------------------------------------------
--
---@class Srendarr_ListItemTemplate : Control
---@field Dimensions {x: layout_measurement, y: layout_measurement}
---@field public OnMouseEnter fun(self: Control)
---@field public OnMouseExit fun(self: Control)
---@field public OnMouseUp fun(self: Control, button: integer, upInside: boolean, ctrl: boolean, alt: boolean, shift: boolean, command: boolean)
Srendarr_ListItemTemplate = {}
-- ---------------------------------------------------------------------------------------------------------------------
--
---@class Srendarr_RecentAuraListFrame : TopLevelWindow
---@field public hidden boolean
---@field Dimensions {x: layout_measurement, y: layout_measurement}
---@field Anchor {point: AnchorPosition, relativeTo: string, relativePoint: AnchorPosition, offsetX: layout_measurement, offsetY: layout_measurement}
Srendarr_RecentAuraListFrame = {}
---------- LVL: 03 ----------
---------- LVL: 04 ----------
-- ---------------------------------------------------------------------------------------------------------------------
--
---@class Srendarr_ListItemTemplateName : LabelControl
---@field public font string
---@field public mouseEnabled boolean
---@field Dimensions {x: layout_measurement, y: layout_measurement}
---@field Anchor {point: AnchorPosition}
---@field public OnMouseEnter fun(self: Control)
---@field public OnMouseExit fun(self: Control)
---@field public OnMouseDown fun(self: Control, button: integer, ctrl: boolean, alt: boolean, shift: boolean, command: boolean)
Srendarr_ListItemTemplateName = {}
-- ---------------------------------------------------------------------------------------------------------------------
--
---@class Srendarr_RecentAuraListFrameBG : BackdropControl
---@field public alpha number
Srendarr_RecentAuraListFrameBG = {}
-- ---------------------------------------------------------------------------------------------------------------------
--
---@class Srendarr_RecentAuraListFrameList : Control
---@field Dimensions {x: layout_measurement, y: layout_measurement}
---@field Anchor {point: AnchorPosition, relativeTo: string, relativePoint: AnchorPosition}
---@field Anchor2 {point: AnchorPosition, relativeTo: string, relativePoint: AnchorPosition}
Srendarr_RecentAuraListFrameList = {}
-- ---------------------------------------------------------------------------------------------------------------------
--
---@class Srendarr_RecentAuraListFrameShowIDs : LabelControl
---@field public font string
---@field public mouseEnabled boolean
---@field Dimensions {x: layout_measurement, y: layout_measurement}
---@field Anchor {point: AnchorPosition, relativeTo: string, relativePoint: AnchorPosition, offsetX: layout_measurement, offsetY: layout_measurement}
---@field public OnMouseEnter fun(self: Control)
---@field public OnMouseExit fun(self: Control)
---@field public OnMouseDown fun(self: Control, button: integer, ctrl: boolean, alt: boolean, shift: boolean, command: boolean)
Srendarr_RecentAuraListFrameShowIDs = {}
-- ---------------------------------------------------------------------------------------------------------------------
--
---@class Srendarr_RecentAuraListFrameCurrentIDs : LabelControl
---@field public font string
---@field public mouseEnabled boolean
---@field Dimensions {x: layout_measurement, y: layout_measurement}
---@field Anchor {point: AnchorPosition, relativeTo: string, relativePoint: AnchorPosition, offsetX: layout_measurement, offsetY: layout_measurement}
---@field public OnMouseEnter fun(self: Control)
---@field public OnMouseExit fun(self: Control)
---@field public OnMouseDown fun(self: Control, button: integer, ctrl: boolean, alt: boolean, shift: boolean, command: boolean)
Srendarr_RecentAuraListFrameCurrentIDs = {}
---------- LVL: 05 ----------
-- ////// END   : GENERATED FROM Srendarr/Srendarr.xml
