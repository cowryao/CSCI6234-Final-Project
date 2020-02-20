package com.OOD.WAMT.Model;

import java.time.LocalDateTime;
import java.util.List;

public class Moderator extends User {
    public List<Group> controlGroups;

    public Moderator(){
        super();
    }
    public void CreateGroup(String NameOfGroup, String DescriptionOfGroup){

    }
    public void Invite(List<String> UserEmails){

    }

    public void Approve(){

    }

    public void PopulateMovies(){

    }

    public void CreateEvent(LocalDateTime startTime, LocalDateTime endTime){

    }

}
