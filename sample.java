package com.example.demo;

import java.util.List;
import java.util.ArrayList;


import java.util.Map;
import java.util.HashMap;

// Multiple empty lines above and below


public class EmptyLineIssues {


    private String name;

    private int age;


    // Constructor with inconsistent empty lines
    public EmptyLineIssues(String name, int age) {

        this.name = name;

        this.age = age;

    }


    // Method with excessive empty lines
    public void processData() {


        List<String> items = new ArrayList<>();


        items.add("item1");

        items.add("item2");


        for (String item : items) {


            System.out.println(item);


        }


    }

    // Another method with inconsistent spacing
    public String getName() {

        return name;

    }


    public void setName(String name) {


        this.name = name;


    }


    // Method with empty lines in wrong places
    public void complexMethod() {
        if (name != null) {

            System.out.println("Name is: " + name);

        } else {

            System.out.println("Name is null");

        }


        try {

            processData();

        } catch (Exception e) {

            e.printStackTrace();

        }


    }


    // Multiple empty lines at end of class


}


// Multiple empty lines at end of file
