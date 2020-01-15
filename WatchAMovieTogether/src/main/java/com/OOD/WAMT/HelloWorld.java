package com.OOD.WAMT;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloWorld {
    @RequestMapping("/index")
    public String Index() {
        return  "Hello World";
    }
}
