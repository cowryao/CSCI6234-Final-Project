package com.OOD.WAMT.Controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller
@RequestMapping(value = "/greeting")
public class GreetingController {
    @RequestMapping( method = RequestMethod.GET)
    public void greeting(ModelMap model) {
        String name = "Kathy Nguyen";
        model.addAttribute("name", name);
        System.out.println("Hello");
    }

}
