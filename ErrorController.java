package com.jtspringproject.JtSpringProject.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

public class CustomErrorController {
 
    public String accessDenied() {
        return "403";
    }
}
