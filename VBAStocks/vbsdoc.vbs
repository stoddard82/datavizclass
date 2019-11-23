

    Dim Col  As Double
    Dim Total_Volume As Double
 
'Heading
    Cells(1, 9).Value = "Ticker"
    Cells(1, 10).Value = "Total Stock Volume"

    Col = 2
    Cells(Col, 9).Value = Cells(Col, 1).Value

    LastRow = Cells(Rows.Count, 1).End(xlUp).Row

    For Row = 2 To LastRow

    If Cells(Row, 1).Value = Cells(Col, 9) Then
    
     
     Total_Volume = Total_Volume + Cells(Row, 7).Value
     
     Else
     
     Cells(Col, 10).Value = Total_Volume
     Total_Volume = Cells(Row, 7).Value
     Col = Col + 1
     Cells(Col, 9).Value = Cells(Row, 1).Value
     End If
     
     Next Row
     
     Cells(Col, 10).Value = Total_Volume
     
End Sub

Sub Moderate_Stock()
  
Dim WS As Worksheet
    For Each WS In ActiveWorkbook.Worksheets
    WS.Activate
        'Last Row
        LastRow = WS.Cells(Rows.Count, 1).End(xlUp).Row

        'Heading for summary
        Cells(1, "I").Value = "Ticker"
        Cells(1, "J").Value = "Yearly Change"
        Cells(1, "K").Value = "Percent Change"
        Cells(1, "L").Value = "Total Stock Volume"
        'Variable to hold Value
        Dim Open_Price As Double
        Dim Close_Price As Double
        Dim Yearly_Change As Double
        Dim Ticker_Name As String
        Dim Percent_Change As Double
        Dim Volume As Double
        Volume = 0
        Dim Row As Double
        Row = 2
        Dim Column As Integer
        Column = 1
        Dim i As Long
        
        'Open Price
        Open_Price = Cells(2, Column + 2).Value
         ' Loop through ticker symbol
        
        For i = 2 To LastRow
         ' Check if still within the same ticker symbol
            If Cells(i + 1, Column).Value <> Cells(i, Column).Value Then
                ' Ticker name
                Ticker_Name = Cells(i, Column).Value
                Cells(Row, Column + 8).Value = Ticker_Name
                ' Close Price
                Close_Price = Cells(i, Column + 5).Value
                ' Yearly Change
                Yearly_Change = Close_Price - Open_Price
                Cells(Row, Column + 9).Value = Yearly_Change
                ' Percent Change
                If (Open_Price = 0 And Close_Price = 0) Then
                    Percent_Change = 0
                ElseIf (Open_Price = 0 And Close_Price <> 0) Then
                    Percent_Change = 1
                Else
                    Percent_Change = Yearly_Change / Open_Price
                    Cells(Row, Column + 10).Value = Percent_Change
                    Cells(Row, Column + 10).NumberFormat = "0.00%"
                End If
                ' Total Volumn
                Volume = Volume + Cells(i, Column + 6).Value
                Cells(Row, Column + 11).Value = Volume
                ' Add one to the summary table row
                Row = Row + 1
                ' reset the Open Price
                Open_Price = Cells(i + 1, Column + 2)
                ' reset the Volumn Total
                Volume = 0
            'cells are the same ticker
            Else
                Volume = Volume + Cells(i, Column + 6).Value
            End If
        Next i
        
        ' Last Row of Yearly Change per WS
        YCLastRow = WS.Cells(Rows.Count, Column + 8).End(xlUp).Row
        ' Cell Colors
        For j = 2 To YCLastRow
            If (Cells(j, Column + 9).Value > 0 Or Cells(j, Column + 9).Value = 0) Then
                Cells(j, Column + 9).Interior.ColorIndex = 10
            ElseIf Cells(j, Column + 9).Value < 0 Then
                Cells(j, Column + 9).Interior.ColorIndex = 3
            End If
        Next j
       
    
        
    Next WS
        


 
End Sub
