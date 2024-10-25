from tkinter import *
import subprocess
text = Tk()
text.title("大小写字母转换器（请输入一个字母）")
text.geometry("400x200")
def close():
    text.destroy
def hanshu1():
    def jiance_password():
        with open('password.txt','r') as file:
            loadpassword = file.read()
        passwd = shuru_password.get()
        if passwd == loadpassword:
            global text
            text.destroy()
            subprocess.run(["python","本体.py"])
        else:
            new.destroy()
    text=shuru.get()    
    if not text:
        no=Toplevel()
        no.title("输出结果")
        no.geometry("250x30")
        nono=Label(no,text="你啥也没输入")
        nono.pack()
        no.mainloop()
    else:
        if text=="a":
            a=Toplevel()
            a.title("输出结果")
            a.geometry("250x30")
            aa=Label(a,text="转换结果为A")
            aa.pack()
            a.mainloop()
        else:
            if text=="b":
                b=Toplevel()
                b.title("输出结果")
                b.geometry("250x30")
                bb=Label(b,text="转换结果为B")
                bb.pack()
                b.mainloop()
            else:
                if text=="c":
                    c=Toplevel()
                    c.title("输出结果")
                    c.geometry("300x30")
                    cc=Label(c,text="转换结果为C")
                    cc.pack()
                    c.mainloop()
                else:
                    if text=="d":
                        d=Toplevel()
                        d.title("输出结果")
                        d.geometry("300x30")
                        dd=Label(d,text="转换结果为D")
                        dd.pack()
                        d.mainloop()
                    else:
                        if text=="e":
                            e=Toplevel()
                            e.title("输出结果")
                            e.geometry("300x30")
                            ee=Label(e,text="转换结果为E")
                            ee.pack()
                            e.mainloop()
                        else:
                            if text=="f":
                                f=Toplevel()
                                f.title("输出结果")
                                f.geometry("300x30")
                                ff=Label(f,text="转换结果为F")
                                ff.pack()
                                f.mainloop()
                            else:
                                if text=="g":
                                    g=Toplevel()
                                    g.title("输出结果")
                                    g.geometry("300x30")
                                    gg=Label(g,text="转换结果为G")
                                    gg.pack()
                                    g.mainloop()
                                else:
                                    if text=="h":
                                        h=Toplevel()
                                        h.title("输出结果")
                                        h.geometry("300x30")
                                        hh=Label(h,text="转换结果为H")
                                        hh.pack()
                                        h.mainloop()
                                    else:
                                        if text=="i":
                                            i=Toplevel()
                                            i.title("输出结果")
                                            i.geometry("300x30")
                                            ii=Label(i,text="转换结果为I")
                                            ii.pack()
                                            i.mainloop()
                                        else:
                                            if text=="j":
                                                j=Toplevel()
                                                j.title("输出结果")
                                                j.geometry("300x30")
                                                jj=Label(j,text="转换结果为J")
                                                jj.pack()
                                                j.mainloop()
                                            else:
                                                if text=="k":
                                                    k=Toplevel()
                                                    k.title("输出结果")
                                                    k.geometry("300x30")
                                                    kk=Label(k,text="转换结果为K")
                                                    kk.pack()
                                                    k.mainloop()
                                                else:
                                                    if text=="l":
                                                        l=Toplevel()
                                                        l.title("输出结果")
                                                        l.geometry("300x30")
                                                        ll=Label(l,text="转换结果为L")
                                                        ll.pack()
                                                        l.mainloop()
                                                    else:
                                                        if text=="m":
                                                            m=Toplevel()
                                                            m.title("输出结果")
                                                            m.geometry("300x30")
                                                            mm=Label(m,text="转换结果为M")
                                                            mm.pack()
                                                            m.mainloop()
                                                        else:
                                                            if text=="n":
                                                                n=Toplevel()
                                                                n.title("输出结果")
                                                                n.geometry("300x30")
                                                                nn=Label(n,text="转换结果为N")
                                                                nn.pack()
                                                                n.mainloop()
                                                            else:
                                                                if text=="o":
                                                                    o=Toplevel()
                                                                    o.title("输出结果")
                                                                    o.geometry("300x30")
                                                                    oo=Label(o,text="转换结果为O")
                                                                    oo.pack()
                                                                    o.mainloop()
                                                                else:
                                                                    if text=="p":
                                                                        p=Toplevel()
                                                                        p.title("输出结果")
                                                                        p.geometry("300x30")
                                                                        pp=Label(p,text="转换结果为P")
                                                                        pp.pack()
                                                                        p.mainloop()
                                                                    else:
                                                                        if text=="q":
                                                                            q=Toplevel()
                                                                            q.title("输出结果")
                                                                            q.geometry("300x30")
                                                                            qq=Label(q,text="转换结果为Q")
                                                                            qq.pack()
                                                                            q.mainloop()
                                                                        else:
                                                                            if text=="r":
                                                                                r=Toplevel()
                                                                                r.title("输出结果")
                                                                                r.geometry("300x30")
                                                                                rr=Label(r,text="转换结果为R")
                                                                                rr.pack()
                                                                                r.mainloop()
                                                                            else:
                                                                                if text=="s":
                                                                                    s=Toplevel()
                                                                                    s.title("输出结果")
                                                                                    s.geometry("300x30")
                                                                                    ss=Label(s,text="转换结果为S")
                                                                                    ss.pack()
                                                                                    s.mainloop()
                                                                                else:
                                                                                    if text=="t":
                                                                                        t=Toplevel()
                                                                                        t.title("输出结果")
                                                                                        t.geometry("300x30")
                                                                                        tt=Label(t,text="转换结果为T")
                                                                                        tt.pack()
                                                                                        t.mainloop()
                                                                                    else:
                                                                                        if text=="u":
                                                                                            u=Toplevel()
                                                                                            u.title("输出结果")
                                                                                            u.geometry("300x30")
                                                                                            uu=Label(u,text="转换结果为U")
                                                                                            uu.pack()
                                                                                            u.mainloop()
                                                                                        else:
                                                                                            if text=="v":
                                                                                                v=Toplevel()
                                                                                                v.title("输出结果")
                                                                                                v.geometry("300x30")
                                                                                                vv=Label(v,text="转换结果为V")
                                                                                                vv.pack()
                                                                                                v.mainloop()
                                                                                            else:
                                                                                                if text=="w":
                                                                                                    w=Toplevel()
                                                                                                    w.title("输出结果")
                                                                                                    w.geometry("300x30")
                                                                                                    ww=Label(w,text="转换结果为W")
                                                                                                    ww.pack()
                                                                                                    w.mainloop()
                                                                                                else:
                                                                                                    if text=="x":
                                                                                                        x=Toplevel()
                                                                                                        x.title("输出结果")
                                                                                                        x.geometry("300x30")
                                                                                                        xx=Label(x,text="转换结果为X")
                                                                                                        xx.pack()
                                                                                                        x.mainloop()
                                                                                                    else:
                                                                                                        if text=="y":
                                                                                                            y=Toplevel()
                                                                                                            y.title("输出结果")
                                                                                                            y.geometry("300x30")
                                                                                                            yy=Label(y,text="转换结果为Y")
                                                                                                            yy.pack()
                                                                                                            y.mainloop()
                                                                                                        else:
                                                                                                            if text=="z":
                                                                                                                z=Toplevel()
                                                                                                                z.title("输出结果")
                                                                                                                z.geometry("300x30")
                                                                                                                zz=Label(z,text="转换结果为Z")
                                                                                                                zz.pack()
                                                                                                                z.mainloop()
                                                                                                            else:
                                                                                                                if text=="A":
                                                                                                                    A=Toplevel()
                                                                                                                    A.title("输出结果")
                                                                                                                    A.geometry("300x30")
                                                                                                                    AA=Label(A,text="转换结果为a")
                                                                                                                    AA.pack()
                                                                                                                    A.mainloop()
                                                                                                                else:
                                                                                                                    if text=="B":
                                                                                                                        B=Toplevel()
                                                                                                                        B.title("输出结果")
                                                                                                                        B.geometry("300x30")
                                                                                                                        BB=Label(B,text="转换结果为b")
                                                                                                                        BB.pack()
                                                                                                                        B.mainloop()
                                                                                                                    else:
                                                                                                                        if text=="C":
                                                                                                                            C=Toplevel()
                                                                                                                            C.title("输出结果")
                                                                                                                            C.geometry("300x30")
                                                                                                                            CC=Label(C,text="转换结果为c")
                                                                                                                            CC.pack()
                                                                                                                            C.mainloop()
                                                                                                                        else:
                                                                                                                            if text=="D":
                                                                                                                                D=Toplevel()
                                                                                                                                D.title("输出结果")
                                                                                                                                D.geometry("300x30")
                                                                                                                                DD=Label(D,text="转换结果为d")
                                                                                                                                DD.pack()
                                                                                                                                D.mainloop()
                                                                                                                            else:
                                                                                                                                if text=="E":
                                                                                                                                    E=Toplevel()
                                                                                                                                    E.title("输出结果")
                                                                                                                                    E.geometry("300x30")
                                                                                                                                    EE=Label(E,text="转换结果为e")
                                                                                                                                    EE.pack()
                                                                                                                                    E.mainloop()
                                                                                                                                else:
                                                                                                                                    if text=="F":
                                                                                                                                        F=Toplevel()
                                                                                                                                        F.title("输出结果")
                                                                                                                                        F.geometry("300x30")
                                                                                                                                        FF=Label(F,text="转换结果为f")
                                                                                                                                        FF.pack()
                                                                                                                                        F.mainloop()
                                                                                                                                    else:
                                                                                                                                        if text=="G":
                                                                                                                                            G=Toplevel()
                                                                                                                                            G.title("输出结果")
                                                                                                                                            G.geometry("300x30")
                                                                                                                                            GG=Label(G,text="转换结果为g")
                                                                                                                                            GG.pack()
                                                                                                                                            G.mainloop()
                                                                                                                                        else:
                                                                                                                                            if text=="H":
                                                                                                                                                H=Toplevel()
                                                                                                                                                H.title("输出结果")
                                                                                                                                                H.geometry("300x30")
                                                                                                                                                HH=Label(H,text="转换结果为h")
                                                                                                                                                HH.pack()
                                                                                                                                                H.mainloop()
                                                                                                                                            else:
                                                                                                                                                if text=="I":
                                                                                                                                                    I=Toplevel()
                                                                                                                                                    I.title("输出结果")
                                                                                                                                                    I.geometry("300x30")
                                                                                                                                                    II=Label(I,text="转换结果为i")
                                                                                                                                                    II.pack()
                                                                                                                                                    I.mainloop()
                                                                                                                                                else:
                                                                                                                                                    if text=="J":
                                                                                                                                                        J=Toplevel()
                                                                                                                                                        J.title("输出结果")
                                                                                                                                                        J.geometry("300x30")
                                                                                                                                                        JJ=Label(J,text="转换结果为j")
                                                                                                                                                        JJ.pack()
                                                                                                                                                        J.mainloop()
                                                                                                                                                    else:
                                                                                                                                                        if text=="K":
                                                                                                                                                            K=Toplevel()
                                                                                                                                                            K.title("输出结果")
                                                                                                                                                            K.geometry("300x30")
                                                                                                                                                            KK=Label(K,text="转换结果为k")
                                                                                                                                                            KK.pack()
                                                                                                                                                            K.mainloop()
                                                                                                                                                        else:
                                                                                                                                                            if text=="L":
                                                                                                                                                                L=Toplevel()
                                                                                                                                                                L.title("输出结果")
                                                                                                                                                                L.geometry("300x30")
                                                                                                                                                                LL=Label(L,text="转换结果为l")
                                                                                                                                                                LL.pack()
                                                                                                                                                                L.mainloop()
                                                                                                                                                            else:
                                                                                                                                                                if text=="M":
                                                                                                                                                                    M=Toplevel()
                                                                                                                                                                    M.title("输出结果")
                                                                                                                                                                    M.geometry("300x30")
                                                                                                                                                                    MM=Label(M,text="转换结果为m")
                                                                                                                                                                    MM.pack()
                                                                                                                                                                    M.mainloop()
                                                                                                                                                                else:
                                                                                                                                                                    if text=="N":
                                                                                                                                                                        N=Toplevel()
                                                                                                                                                                        N.title("输出结果")
                                                                                                                                                                        N.geometry("300x30")
                                                                                                                                                                        NN=Label(N,text="转换结果为n")
                                                                                                                                                                        NN.pack()
                                                                                                                                                                        N.mainloop()
                                                                                                                                                                    else:
                                                                                                                                                                        if text=="O":
                                                                                                                                                                            O=Toplevel()
                                                                                                                                                                            O.title("输出结果")
                                                                                                                                                                            O.geometry("300x30")
                                                                                                                                                                            OO=Label(O,text="转换结果为o")
                                                                                                                                                                            OO.pack()
                                                                                                                                                                            O.mainloop()
                                                                                                                                                                        else:
                                                                                                                                                                            if text=="P":
                                                                                                                                                                                P=Toplevel()
                                                                                                                                                                                P.title("输出结果")
                                                                                                                                                                                P.geometry("300x30")
                                                                                                                                                                                PP=Label(P,text="转换结果为p")
                                                                                                                                                                                PP.pack()
                                                                                                                                                                                P.mainloop()
                                                                                                                                                                            else:
                                                                                                                                                                                if text=="Q":
                                                                                                                                                                                        Q=Toplevel()
                                                                                                                                                                                        Q.title("输出结果")
                                                                                                                                                                                        Q.geometry("300x30")
                                                                                                                                                                                        QQ=Label(Q,text="转换结果为q")
                                                                                                                                                                                        QQ.pack()
                                                                                                                                                                                        Q.mainloop()
                                                                                                                                                                                else:
                                                                                                                                                                                    if text=="R":
                                                                                                                                                                                        R=Toplevel()
                                                                                                                                                                                        R.title("输出结果")
                                                                                                                                                                                        R.geometry("300x30")
                                                                                                                                                                                        RR=Label(R,text="转换结果为r")
                                                                                                                                                                                        RR.pack()
                                                                                                                                                                                        R.mainloop()
                                                                                                                                                                                    else:
                                                                                                                                                                                        if text=="S":
                                                                                                                                                                                            S=Toplevel()
                                                                                                                                                                                            S.title("输出结果")
                                                                                                                                                                                            S.geometry("300x30")
                                                                                                                                                                                            SS=Label(S,text="转换结果为s")
                                                                                                                                                                                            SS.pack()
                                                                                                                                                                                            S.mainloop()
                                                                                                                                                                                        else:
                                                                                                                                                                                            if text=="T":
                                                                                                                                                                                                T=Toplevel()
                                                                                                                                                                                                T.title("输出结果")
                                                                                                                                                                                                T.geometry("300x30")
                                                                                                                                                                                                TT=Label(T,text="转换结果为t")
                                                                                                                                                                                                TT.pack()
                                                                                                                                                                                                T.mainloop()
                                                                                                                                                                                            else:
                                                                                                                                                                                                if text=="U":
                                                                                                                                                                                                    U=Toplevel()
                                                                                                                                                                                                    U.title("输出结果")
                                                                                                                                                                                                    U.geometry("300x30")
                                                                                                                                                                                                    UU=Label(U,text="转换结果为u")
                                                                                                                                                                                                    UU.pack()
                                                                                                                                                                                                    U.mainloop()
                                                                                                                                                                                                else:
                                                                                                                                                                                                    if text=="V":
                                                                                                                                                                                                        V=Toplevel()
                                                                                                                                                                                                        V.title("输出结果")
                                                                                                                                                                                                        V.geometry("300x30")
                                                                                                                                                                                                        VV=Label(V,text="转换结果为v")
                                                                                                                                                                                                        VV.pack()
                                                                                                                                                                                                        V.mainloop()
                                                                                                                                                                                                    else:
                                                                                                                                                                                                        if text=="W":
                                                                                                                                                                                                            W=Toplevel()
                                                                                                                                                                                                            W.title("输出结果")
                                                                                                                                                                                                            W.geometry("300x30")
                                                                                                                                                                                                            WW=Label(W,text="转换结果为w")
                                                                                                                                                                                                            WW.pack()
                                                                                                                                                                                                            W.mainloop()
                                                                                                                                                                                                        else:
                                                                                                                                                                                                            if text=="X":
                                                                                                                                                                                                                X=Toplevel()
                                                                                                                                                                                                                X.title("输出结果")
                                                                                                                                                                                                                X.geometry("300x30")
                                                                                                                                                                                                                XX=Label(X,text="转换结果为x")
                                                                                                                                                                                                                XX.pack()
                                                                                                                                                                                                                X.mainloop()
                                                                                                                                                                                                            else:
                                                                                                                                                                                                                if text=="Y":
                                                                                                                                                                                                                    Y=Toplevel()
                                                                                                                                                                                                                    Y.title("输出结果")
                                                                                                                                                                                                                    Y.geometry("300x30")
                                                                                                                                                                                                                    YY=Label(Y,text="转换结果为y")
                                                                                                                                                                                                                    YY.pack()
                                                                                                                                                                                                                    Y.mainloop()
                                                                                                                                                                                                                else:
                                                                                                                                                                                                                    if text=="Z":
                                                                                                                                                                                                                        Z=Toplevel()
                                                                                                                                                                                                                        Z.title("输出结果")
                                                                                                                                                                                                                        Z.geometry("300x30")
                                                                                                                                                                                                                        ZZ=Label(Z,text="转换结果为z")
                                                                                                                                                                                                                        ZZ.pack()
                                                                                                                                                                                                                        Z.mainloop()
                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                        if text=="root":
                                                                                                                                                                                                                            new=Toplevel()
                                                                                                                                                                                                                            new.title("输入密码")
                                                                                                                                                                                                                            new.geometry("300x100")
                                                                                                                                                                                                                            label2=Label(new,text="特殊登录模式")
                                                                                                                                                                                                                            label2.pack()
                                                                                                                                                                                                                            shuru_password=Entry(new,show="*")
                                                                                                                                                                                                                            shuru_password.pack()
                                                                                                                                                                                                                            an=Button(new,text="确认",command=jiance_password)
                                                                                                                                                                                                                            an.pack()
                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                            other=Toplevel()
                                                                                                                                                                                                                            other.title("输出结果")
                                                                                                                                                                                                                            other.geometry("300x30")
                                                                                                                                                                                                                            otherother=Label(other, text="转换结果为其他字符")
                                                                                                                                                                                                                            otherother.pack()
bianliang=StringVar()
label=Label(text,text="输入一个字母，输入特殊内容进入特殊模式")
label.pack()
shuru=Entry(text,width=50,textvariable=bianliang)
shuru.pack()
button=Button(text,text='确定',command=hanshu1,width=20,height=5)
button.pack()
text.mainloop()