#############################################################################
# Generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#  Dec 05, 2019 06:21:30 PM -0300  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}




proc vTclWindow.top42 {base} {
    global vTcl
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 846x549+337+125
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1362 741
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    button $top.but43 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Instala 
    vTcl:DefineAlias "$top.but43" "Instala" vTcl:WidgetProc "Toplevel1" 1
    bind $top.but43 <Button-1> {
        lambda e: ButtonMouse1Instala(e)
    }
    listbox $top.lis44 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -height 382 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -selectbackground #c4c4c4 -selectforeground black -width 364 
    .top42.lis44 configure -font "TkFixedFont"
    .top42.lis44 insert end text
    vTcl:DefineAlias "$top.lis44" "LogDll" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $top.tCo45 \
        -values 1 2 3 4 5 6 -font TkTextFont -textvariable combobox \
        -foreground {} -background {} -takefocus {} 
    vTcl:DefineAlias "$top.tCo45" "cmbOper" vTcl:WidgetProc "Toplevel1" 1
    bind $top.tCo45 <<ComboboxSelected>> {
        lambda e: ComboboxSelectedCmbOper(e)
    }
    listbox $top.lis46 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -height 292 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -selectbackground #c4c4c4 -selectforeground black -width 354 
    .top42.lis46 configure -font "TkFixedFont"
    .top42.lis46 insert end text
    vTcl:DefineAlias "$top.lis46" "lstParameters" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab47 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text PWINFO__OPERATION 
    vTcl:DefineAlias "$top.lab47" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab48 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text PARÂMETROS: 
    vTcl:DefineAlias "$top.lab48" "Label2" vTcl:WidgetProc "Toplevel1" 1
    button $top.but49 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Remover 
    vTcl:DefineAlias "$top.but49" "btnRemover" vTcl:WidgetProc "Toplevel1" 1
    bind $top.but49 <Button-1> {
        lambda e: ButtonMouse1btnRemover(e)
    }
    button $top.but50 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Adicionar 
    vTcl:DefineAlias "$top.but50" "btnAdicionar" vTcl:WidgetProc "Toplevel1" 1
    bind $top.but50 <Button-1> {
        lambda e: ButtonMouse1btnAdicionar(e)
    }
    button $top.but51 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Limpar 
    vTcl:DefineAlias "$top.but51" "btnLimpar" vTcl:WidgetProc "Toplevel1" 1
    bind $top.but51 <Button-1> {
        lambda e: ButtonMouse1btnLimpar(e)
    }
    button $top.but52 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {Captura PinPad} 
    vTcl:DefineAlias "$top.but52" "btnCaptura" vTcl:WidgetProc "Toplevel1" 1
    bind $top.but52 <Button-1> {
        lambda e: ButtonMouse1btnCaptura(e)
    }
    button $top.but53 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Executar 
    vTcl:DefineAlias "$top.but53" "btnExecutar" vTcl:WidgetProc "Toplevel1" 1
    bind $top.but53 <Button-1> {
        lambda e: ButtonMouse1btnExecutar(e)
    }
    button $top.but54 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {Limpa Log} 
    vTcl:DefineAlias "$top.but54" "btnLimpaLog" vTcl:WidgetProc "Toplevel1" 1
    bind $top.but54 <Button-1> {
        lambda e: ButtonMouse1btnLimpaLog(e)
    }
    label $top.lab43 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {LOG de Eventos da DLL} 
    vTcl:DefineAlias "$top.lab43" "Label3" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but43 \
        -in $top -x 40 -y 10 -width 67 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lis44 \
        -in $top -x 440 -y 40 -width 364 -relwidth 0 -height 382 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tCo45 \
        -in $top -x 170 -y 50 -width 213 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lis46 \
        -in $top -x 40 -y 120 -width 354 -relwidth 0 -height 292 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 40 -y 50 -anchor nw -bordermode ignore 
    place $top.lab48 \
        -in $top -x 40 -y 90 -width 85 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but49 \
        -in $top -x 170 -y 90 -width 87 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but50 \
        -in $top -x 290 -y 90 -width 87 -height 24 -anchor nw \
        -bordermode ignore 
    place $top.but51 \
        -in $top -x 40 -y 420 -width 68 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but52 \
        -in $top -x 120 -y 420 -width 93 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but53 \
        -in $top -x 240 -y 420 -anchor nw -bordermode ignore 
    place $top.but54 \
        -in $top -x 440 -y 440 -width 77 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab43 \
        -in $top -x 560 -y 10 -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

