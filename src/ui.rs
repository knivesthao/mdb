//! Slint UI shell (plan step 10, host part): login, hardware/intent,
//! and server-dashboard screens. Static placeholders for now — real
//! scanner values get wired in when the Android shell lands (step 12).

slint::include_modules!();

use std::{cell::RefCell, rc::Rc};

pub fn run() {
    let ui = MainWindow::new().unwrap();

    let running = Rc::new(RefCell::new(false));
    ui.on_start_pressed({
        let ui_weak = ui.as_weak();
        let running = running.clone();
        move || {
            let ui = ui_weak.unwrap();
            let mut r = running.borrow_mut();
            *r = !*r;
            ui.set_server_status(if *r { "Running".into() } else { "Stopped".into() });
        }
    });

    ui.on_recommend_pressed({
        let ui_weak = ui.as_weak();
        move || {
            ui_weak.unwrap().set_recommended_model("qwen2.5-coder-1.5b".into());
        }
    });

    ui.run().unwrap();
}
