Clazz.declarePackage ("J.script");
Clazz.load (["J.thread.JmolThread"], "J.script.CommandWatcherThread", ["java.lang.Thread", "JW.Logger"], function () {
c$ = Clazz.decorateAsClass (function () {
this.scriptManager = null;
Clazz.instantialize (this, arguments);
}, J.script, "CommandWatcherThread", J.thread.JmolThread);
Clazz.makeConstructor (c$, 
function () {
Clazz.superConstructor (this, J.script.CommandWatcherThread, []);
});
Clazz.overrideMethod (c$, "setManager", 
function (manager, vwr, params) {
this.scriptManager = manager;
this.setViewer (vwr, "CommmandWatcherThread");
return 0;
}, "~O,JV.Viewer,~O");
Clazz.overrideMethod (c$, "run", 
function () {
Thread.currentThread ().setPriority (1);
while (!this.stopped) {
try {
Thread.sleep (50);
if (!this.stopped) {
this.scriptManager.runScriptNow ();
}} catch (e$$) {
if (Clazz.exceptionOf (e$$, InterruptedException)) {
var ie = e$$;
{
JW.Logger.warn ("CommandWatcher InterruptedException! " + this);
break;
}
} else if (Clazz.exceptionOf (e$$, Exception)) {
var ie = e$$;
{
var s = "script processing ERROR:\n\n" + ie.toString ();
for (var i = 0; i < ie.getStackTrace ().length; i++) {
s += "\n" + ie.getStackTrace ()[i].toString ();
}
JW.Logger.warn ("CommandWatcher Exception! " + s);
break;
}
} else {
throw e$$;
}
}
}
});
Clazz.overrideMethod (c$, "run1", 
function (mode) {
}, "~N");
Clazz.defineStatics (c$,
"commandDelay", 50);
});
