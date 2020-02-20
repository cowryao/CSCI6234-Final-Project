package com.OOD.WAMT.Controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.Arrays;
import java.util.List;

@Controller
public class HomePageController {
    @RequestMapping("/")
    public String index(
            @RequestParam(value = "participant", required = false) String participant,
            @RequestParam(value = "country", required = false) String country,
            @RequestParam(value = "action", required = false) String action,
            @RequestParam(value = "id", required = false) Integer id,
            Model model
    ) {
        model.addAttribute("id", id);
        List<Integer> userIds = Arrays.asList(1,2,3,4);
        model.addAttribute("userIds", userIds);
        System.out.println(participant);
        return "index";
    }
}
